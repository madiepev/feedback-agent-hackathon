# Phase 4: Iteration

**Duration:** ~25 minutes  
**Time:** 20:15-20:40  
**Goal:** Improve your agent based on feedback received

---

## Step 1: Review Feedback (10 min)

### Find Your Feedback:
1. Go to the **Issues** tab in the main hackathon repository
2. Filter or search for issues about your group: `"Group [X]"` in title
3. Open the feedback issue created by the team that tested your agent

### Read Carefully:
- What did they find helpful?
- What was unclear or unhelpful?
- What was their overall rating?
- What concrete example did they provide?
- What ONE thing did they suggest you change?

### Discuss as a Team:
- Do we agree with the feedback?
- What should we prioritize fixing?
- What 1-3 changes will have the biggest impact?

---

## Step 2: Identify Improvements (5 min)

Based on the feedback, prioritize **1-3 specific changes**:

### Common Issues & Fixes:

**Issue:** "Too vague"  
**Fix:** Add instructions to quote specific phrases from the summary

**Issue:** "Didn't use the rubric"  
**Fix:** Require agent to evaluate each of the 5 dimensions explicitly

**Issue:** "Too harsh/demotivating"  
**Fix:** Add instruction to start with positive observations

**Issue:** "Not actionable"  
**Fix:** Require concrete revision suggestions with examples

**Issue:** "Too much at once"  
**Fix:** Prioritize - tell agent to identify the 1-2 most important issues first

---

## Step 3: Revise Your Agent (12 min)

### Edit Your Instruction File:

1. Open `.github/instructions/group[X]-feedback-agent.md`
2. Make your improvements
3. Consider adding:
   - More specific guidelines
   - Examples of good feedback
   - Constraints (e.g., "always quote the text")
   - Structure requirements (e.g., "organize by rubric dimension")

### Test Your Changes:

1. Open GitHub Copilot Chat
2. Test with the same summary from Phase 1
3. Verify the feedback is better:
   - More specific?
   - More actionable?
   - Better tone?
   - Uses rubric?

### Iterate:
- If still not right, adjust again
- Test until satisfied

---

## Step 4: Document Your Changes (Optional)

Consider adding a comment at the top of your file:

```markdown
## Version 2 Changes (Phase 4)
- Added explicit rubric scoring
- Now quotes specific phrases from the summary
- Starts with positive observations
- Prioritizes top 2 issues
```

---

## Step 5: Commit v2 (3 min)

### Save Your Improvements:

**Via GitHub Web:**
1. Click **Commit changes**
2. Message: `"Iteration based on Phase 3 feedback"`
3. Click **Commit changes**

**Via Git CLI:**
```bash
git add .github/instructions/
git commit -m "v2: Iteration based on Phase 3 feedback"
git push
```

---

## ✅ Agent Improved!

Your agent is now refined and ready for community testing in Phase 5.

**Next:** [Phase 5: Community Testing & Reflection →](phase5-showcase.md)
