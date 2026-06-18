# Agent Instructions Folder

This folder contains agent instruction files created during the hackathon.

## How to Create Your Agent

**In GitHub Copilot Chat:**
1. Click the **+** button at bottom of message box
2. Click **Instructions**
3. Click **Configure Instructions**
4. Click **+ New Instruction file**
5. Choose `.github/instructions` (default)
6. Name with your group number: `group1-feedback-agent.instructions.md`, `group2-feedback-agent.instructions.md`, etc.

## What to Include

Define how your agent should give feedback on science writing summaries:

- **Role**: What persona should the agent adopt?
- **Approach**: How should it use the Universal Science Writing Rubric?
- **Tone**: Formal? Friendly? Socratic?
- **Structure**: Step-by-step? All at once? Question-based?
- **Examples**: Show what good feedback looks like

## Testing Your Agent

In GitHub Copilot Chat:
```
Give me feedback on this summary:

[paste your summary here]
```

GitHub Copilot will automatically use your instructions file.
