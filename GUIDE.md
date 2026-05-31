# Hackathon Guide

**3-hour sprint to build and test your AI feedback agent**

---

## Before You Start

### You'll Need:
- GitHub account
- GitHub Copilot enabled (or [start free trial](https://github.com/features/copilot))

**Note:** You'll fork the repository AFTER Phase 1 — your peer summaries from Discussions will become your agent's test data!

---

## Phase 1: Orientation & Elicitation (~50 min)

### Read & Write (15 min)
1. Go to **Discussions** tab in this repository
2. Open the pinned discussion: **"Phase 1: Share Your Summary"**
3. Read [assets/article.md](assets/article.md) (Mars geology findings)
4. Write a 50-100 word summary of the main scientific findings
5. **Post your summary as a comment** in the discussion

### Vote for Best Summary (5 min)
- Refresh the discussion page
- Read your peers' summaries
- React with 👍 to the one you think is strongest
- Facilitator will show which got the most votes

### Identify Quality (10 min)
**Group Discussion:** Why did those summaries get the most votes?
- What made them good?
- What specific features stood out (accuracy, clarity, evidence, etc.)?

**Group Discussion:** How could lower-voted summaries improve?
- What's missing or unclear?
- What would you change?

### Learn the Rubric (8 min)
Facilitator introduces the **Universal Science Writing Rubric**:
- 5 dimensions of quality science writing
- Shows how your intuitions align with research-based criteria
- Open [assets/rubric.md](assets/rubric.md) for reference

### Evaluate Example (5 min)
1. Go back to **Discussions** tab
2. Open: **"Phase 1: Evaluate the Example Summary Using the Rubric"**
3. Read the example summary shown in the discussion
4. **Vote on all 5 polls** (one per rubric dimension)
5. Discuss: How did using the rubric compare to your initial instincts?

### FeedbackFruits Presentation (~10 min)
Learn about FeedbackFruits' approach to educational feedback tools.

### Fork Repository (~2 min)
Now that you've created summaries together in the Discussions:
1. Click **Fork** at the top of this repository
2. You now have access to real peer summaries to test your agent with!

**Key Insight:** You've now experienced what AI feedback agents need to do — recognize quality, explain why, and suggest improvements using clear criteria.

---

## Phase 2: Agent Design (~50 min)

### Design Your Agent (35 min)

**Create your instructions file:**
1. In GitHub Copilot Chat, click the **+** button at bottom of message box
2. Click **Instructions**
3. Click **Configure Instructions**
4. Click **+ New Instruction file**
5. Name it with your group number (e.g., `group1-feedback-agent.md`, `group2-feedback-agent.md`)
6. Write your agent's behavior rules

**Key Decisions:**
- What type of feedback? (corrections, questions, guidance)
- How to use the rubric? (score first, focus on specific dimensions)
- What tone? (coach, peer, editor)
- How detailed?
- All at once or step-by-step?

### Test Your Agent (10 min)
1. Open GitHub Copilot Chat in your repository
2. Paste your summary from Phase 1
3. Ask: "Give me feedback on this summary"
4. Adjust your instructions if needed

### Commit (5 min)
Save your changes to GitHub (click "Commit changes" or use git)

---

## Phase 3: Cross-Testing (~25 min)

### Test Another Team's Agent (10 min)
- Facilitator assigns you another team's repository
- Use their agent on YOUR summary
- Note: What works? What doesn't?

### Submit Feedback via GitHub Issue (15 min)
1. Go to **Issues** tab in the main repository
2. Click **New Issue**
3. Select **"Agent Feedback (Phase 3)"** template
4. Choose your group and the group you're evaluating from dropdowns
5. Describe strengths, gaps, and suggestions

---

## Phase 4: Iteration (~30 min)

### Review Feedback (10 min)
- Check the **Issues** tab in YOUR repository
- Read what other teams said
- Discuss: What should we change?

### Revise Your Agent (15 min)
- Update your agent instructions file in `.github/`
- Document what you changed and why
- Test again with Copilot Chat

### Commit v2 (5 min)
Save your improved version

---

## Phase 5: Showcase & Vote (~25 min)

### Gallery Walk (15 min)
- Set up at your station
- Let others test your agent
- Try other teams' agents on your summary

### Vote (10 min)
- Vote for the most effective agent (not your own)
- Consider: usefulness, specificity, rubric use, tone

**Winner announced!**

---

## Need Help?

**During the event:** Ask a facilitator  
**Technical issues:** Use GitHub web interface (no git commands needed)  
**Research questions:** See [CONSENT.md](CONSENT.md)
