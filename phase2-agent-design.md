# Phase 2: Agent Design

**Duration:** ~45 minutes  
**Time:** 19:05-19:50  
**Goal:** Build your AI feedback agent using GitHub Copilot instructions

---

## Step 1: Design Your Agent Strategy (10 min)

Before coding, decide on your agent's approach:

### Key Design Decisions:

**1. Feedback Type**
- Corrections (fix errors directly)
- Questions (guide reflection)
- Guidance (suggest approaches)
- Mix of all three?

**2. Rubric Usage**
- Score each dimension first?
- Focus on weakest dimension?
- Evaluate all 5 dimensions?
- Provide overall score?

**3. Tone**
- Coach (encouraging, supportive)
- Peer (casual, collaborative)
- Editor (direct, professional)
- Teacher (explanatory, educational)

**4. Specificity Level**
- Quote specific phrases from the summary
- Provide concrete examples
- Give general observations
- Suggest specific revisions?

**5. Structure**
- All feedback at once?
- Step-by-step questions?
- Prioritize most important issues?

---

## Step 2: Create Your Instruction File (20 min)

### Setup:

1. Open your **forked repository** in VS Code or GitHub web interface
2. In GitHub Copilot Chat, click the **+** button at bottom of message box
3. Click **Instructions**
4. Click **Configure Instructions**
5. Click **+ New Instruction file**
6. Name it: `.github/instructions/group[X]-feedback-agent.md` (replace [X] with your group number)

### Write Your Agent Instructions

Your instruction file tells GitHub Copilot how to behave when giving feedback.

**Example template:**

```markdown
# Science Writing Feedback Agent - Group [X]

You are a feedback agent for science writing summaries.

## Your Role
[Coach/Peer/Editor] helping students improve their summaries

## Process
1. [First step - e.g., "Read the summary carefully"]
2. [Second step - e.g., "Evaluate against the rubric"]
3. [Third step - e.g., "Provide specific feedback"]

## Using the Rubric
- Reference the Universal Science Writing Rubric (5 dimensions)
- [Specify how - score each? focus on weakest? etc.]

## Feedback Style
- Tone: [encouraging/direct/questioning]
- Specificity: [Quote their text/provide examples]
- Structure: [All at once/step-by-step/prioritized]

## What to Include
- [e.g., "Identify what's working well"]
- [e.g., "Point out missing elements"]
- [e.g., "Suggest concrete improvements"]
- [e.g., "Provide revision examples"]

## What to Avoid
- [e.g., "Don't rewrite the entire summary"]
- [e.g., "Don't be overly critical"]
```

---

## Step 3: Test Your Agent (10 min)

1. Open **GitHub Copilot Chat** in your repository
2. Paste **your summary from Phase 1**
3. Ask: `"Give me feedback on this summary"`
4. Review the feedback you get

**Ask yourself:**
- Is it helpful?
- Is it specific enough?
- Does it use the rubric?
- Would you know how to improve based on this?

### Adjust if needed:
- Refine your instructions
- Test again
- Iterate until satisfied

---

## Step 4: Commit Your Changes (5 min)

### Via GitHub Web Interface:
1. Navigate to your file in `.github/instructions/`
2. Click **Commit changes**
3. Add commit message: "Add feedback agent instructions v1"
4. Click **Commit changes**

### Via Git Command Line:
```bash
git add .github/instructions/
git commit -m "Add feedback agent instructions v1"
git push
```

---

## ✅ You're Ready!

Your agent is now ready to be tested by another team in Phase 3.

**Next:** [Phase 3: Cross-Testing →](phase3-cross-testing.md)
