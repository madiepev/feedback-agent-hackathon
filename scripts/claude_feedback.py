#!/usr/bin/env python3
"""Run Claude feedback using workshop instructions and local rubric assets."""

from __future__ import annotations

import argparse
import json
import os
import sys
import textwrap
import urllib.error
import urllib.request
from pathlib import Path


ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate science-writing feedback with Claude."
    )
    parser.add_argument(
        "--instructions-path",
        required=True,
        help="Path under .github/instructions to the group instruction file.",
    )
    parser.add_argument(
        "--summary",
        required=True,
        help="Student summary text to give feedback on.",
    )
    parser.add_argument(
        "--model",
        default="claude-sonnet-4-6",
        help="Anthropic model name.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=1200,
        help="Maximum output tokens for Claude.",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Trusted repository root containing assets and this script.",
    )
    parser.add_argument(
        "--output",
        default="claude-feedback.md",
        help="Markdown file to write feedback to.",
    )
    return parser.parse_args()


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def resolve_instruction(root: Path, path_text: str) -> Path:
    raw_path = Path(path_text)
    if raw_path.is_absolute():
        fail("instructions_path must be relative, not absolute")

    normalized = Path(os.path.normpath(path_text))
    if normalized.parts[:2] != (".github", "instructions"):
        fail("instructions_path must point inside .github/instructions")

    resolved_root = root.resolve()
    resolved_path = (resolved_root / normalized).resolve()
    try:
        resolved_path.relative_to(resolved_root)
    except ValueError:
        fail("instructions_path must not escape the instructions repository")

    if not resolved_path.is_file():
        fail(f"instruction file does not exist: {normalized}")
    return resolved_path


def read_required_file(path: Path, label: str) -> str:
    if not path.is_file():
        fail(f"missing required {label}: {path}")
    return path.read_text(encoding="utf-8")


def build_prompt(
    instructions: str,
    rubric: str,
    article: str,
    summary: str,
) -> tuple[str, str]:
    system_prompt = textwrap.dedent(
        """
        You are a workshop feedback assistant for science writing summaries.
        Follow the group-authored instructions exactly where they define role,
        tone, structure, and feedback strategy. Use the Universal Science
        Writing Rubric and the article context as the source of truth. Give
        specific, actionable feedback on the pasted student summary without
        rewriting the entire summary for the student.
        """
    ).strip()

    user_prompt = textwrap.dedent(
        f"""
        <group_instructions>
        {instructions}
        </group_instructions>

        <rubric>
        {rubric}
        </rubric>

        <article_context>
        {article}
        </article_context>

        <student_summary>
        {summary}
        </student_summary>

        Give feedback on the student summary now.
        """
    ).strip()

    return system_prompt, user_prompt


def call_claude(
    api_key: str,
    model: str,
    max_tokens: int,
    system_prompt: str,
    user_prompt: str,
) -> str:
    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "system": system_prompt,
        "messages": [
            {
                "role": "user",
                "content": user_prompt,
            }
        ],
    }

    request = urllib.request.Request(
        ANTHROPIC_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "x-api-key": api_key,
            "anthropic-version": ANTHROPIC_VERSION,
            "content-type": "application/json",
            "accept": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            response_body = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        fail(f"Anthropic API returned HTTP {error.code}: {body}")
    except urllib.error.URLError as error:
        fail(f"could not reach Anthropic API: {error.reason}")

    data = json.loads(response_body)
    text_parts = [
        block.get("text", "")
        for block in data.get("content", [])
        if block.get("type") == "text"
    ]
    feedback = "\n\n".join(part for part in text_parts if part).strip()
    if not feedback:
        fail("Anthropic API response did not contain text feedback")
    return feedback


def write_outputs(output_path: Path, feedback: str) -> None:
    output_path.write_text(feedback + "\n", encoding="utf-8")

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary_file:
            summary_file.write("## Claude Feedback\n\n")
            summary_file.write(feedback)
            summary_file.write("\n")


def main() -> None:
    args = parse_args()

    if args.max_tokens < 1 or args.max_tokens > 4096:
        fail("--max-tokens must be between 1 and 4096")

    repo_root = Path(args.repo_root)
    instruction_path = resolve_instruction(repo_root, args.instructions_path)

    instructions = read_required_file(instruction_path, "instruction file")
    rubric = read_required_file(repo_root / "assets" / "rubric.md", "rubric")
    article = read_required_file(repo_root / "assets" / "article.md", "article")

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        fail("ANTHROPIC_API_KEY is not set")

    system_prompt, user_prompt = build_prompt(
        instructions=instructions,
        rubric=rubric,
        article=article,
        summary=args.summary,
    )
    feedback = call_claude(
        api_key=api_key,
        model=args.model,
        max_tokens=args.max_tokens,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
    )
    write_outputs(Path(args.output), feedback)


if __name__ == "__main__":
    main()
