# Facilitator Notes

**Event:** Can AI Give Good Feedback? Build One and Find Out  
**Duration:** 3 hours  
**Date:** June 17, 2026

---

## Pre-Event Setup

### GitHub Discussions Preparation

Create two GitHub Discussions in your repository before the event:

**Discussion 1: Share Your Summary**
- **Title:** Phase 1: Share Your Mars Summary
- **Category:** General
- **Body:**
```markdown
Welcome! Before building feedback agents, let's create test data together.

## Your Task
1. Read [assets/article.md](../blob/main/assets/article.md)
2. Write a 50-100 word summary of the main scientific findings
3. Post your summary as a **comment below**
4. Read others' summaries and react with 👍 to your favorite

## Rules
- One summary per person
- 50-100 words only
- Focus on the science (not background/context)
- Post by [TIME] — we'll count votes together!
```

**Discussion 2: Evaluate the Example Summary**
- **Title:** Phase 1: Evaluate the Example Summary Using the Rubric
- **Category:** Polls
- **Body:**
```markdown
Now that you've learned the Universal Science Writing Rubric, let's practice!

Read this example summary (from [assets/example-summary.md](../blob/main/assets/example-summary.md)):

> NASA's Perseverance rover discovered the "Bright Angel" rock formation in Jezero Crater, revealing diverse redox chemistry through Raman and fluorescence spectroscopy. Multiple minerals indicate dynamic wet-dry cycles during Mars' early history. Organic matter detection suggests complex prebiotic chemistry, though biological origin remains unconfirmed. These findings constrain models of Mars' ancient climate and aqueous geochemistry, with implications for understanding planetary habitability beyond Earth.

**Vote on each dimension below (1=Absent, 2=Developing, 3=Proficient, 4=Mastery):**
```

- **Poll 1:** Dimension A - Content Accuracy (Options: 1-Absent, 2-Developing, 3-Proficient, 4-Mastery)
- **Poll 2:** Dimension B - Interpretation (Options: 1-Absent, 2-Developing, 3-Proficient, 4-Mastery)
- **Poll 3:** Dimension C - Audience Targeting (Options: 1-Absent, 2-Developing, 3-Proficient, 4-Mastery)
- **Poll 4:** Dimension D - Organization (Options: 1-Absent, 2-Developing, 3-Proficient, 4-Mastery)
- **Poll 5:** Dimension E - Writing Quality (Options: 1-Absent, 2-Developing, 3-Proficient, 4-Mastery)

### Materials Checklist
- [ ] Discussion 1 (Share Your Summary) created and pinned
- [ ] Discussion 2 (Evaluate Example) created with 5 polls
- [ ] Projector/screen for displaying discussion responses live
- [ ] GitHub Copilot access verified for all participants
- [ ] Team assignments prepared (3-4 people per team)
- [ ] Cross-testing assignments ready (which team tests which)

---

## Phase 1: Orientation & Elicitation (~50 min)

### Timeline:
- **0:00-0:05** — Welcome & introduce GitHub Discussions workflow
- **0:05-0:15** — Silent reading & writing summaries
- **0:15-0:20** — Post summaries to Discussion, read peers' work, upvote favorites
- **0:20-0:25** — Identify most popular summaries and discuss what made them good
- **0:25-0:30** — Discuss how to improve weaker summaries
- **0:30-0:38** — Introduce the Universal Science Writing Rubric
- **0:38-0:43** — Vote on example summary using Discussion polls
- **0:43-0:53** — FeedbackFruits presentation
- **0:53-0:55** — Fork repository

### Facilitator Script:

**Introduction (5 min):**
> "Before we build AI feedback agents, let's experience the task ourselves. Navigate to the Discussions tab—I've pinned 'Phase 1: Share Your Summary' at the top. Read the Mars article (assets/article.md), then write a 50-100 word summary and post it as a comment. You have 10 minutes."

**After posting period (5 min):**
> "Now refresh the discussion. Read your peers' summaries. React with 👍 to the one you think is strongest. Trust your instincts—we'll analyze why later."
>
> [Give 2-3 minutes for voting, then refresh and sort by reactions]

**Quality discussion (5 min):**
> "Let's look at the top-voted summaries. [Read top 2-3 aloud]. What made these good? Call out specific features."
> 
> [Collect responses verbally, write themes on board/screen: accuracy, clarity, completeness, evidence, etc.]
> 
> "Notice these patterns—you're already experts at recognizing quality!"

**Improvement discussion (5 min):**
> "Now look at summaries with fewer votes. What could they improve? What's missing or unclear?"
>
> [Collect responses, highlight themes: vague language, missing evidence, too much background, etc.]
>
> "Great—you've just done what feedback agents need to do: identify quality AND explain how to improve."

**Rubric introduction (8 min):**
> "Your intuitions align with research. Let me introduce the Universal Science Writing Rubric—it formalizes the criteria you just discovered."
>
> [Walk through 5 dimensions: Content Accuracy, Interpretation, Audience, Organization, Writing Quality]
>
> "This rubric is your agent's foundation. Your job is to decide HOW it should use these criteria to help students."

**Example evaluation (5 min):**
> "Navigate to the second pinned discussion: 'Evaluate the Example Summary'. You'll see an example summary and 5 polls—one per rubric dimension. Vote on each dimension. How does using the rubric compare to your gut instinct?"
>
> [Allow 3-4 minutes for voting]
>
> "Let's see the results. [Review poll results] Notice how the rubric helps us be specific about strengths and weaknesses."

**FeedbackFruits Presentation (10 min):**
> "Now let's hear from FeedbackFruits about how they approach educational feedback tools."
>
> [Hand off to FeedbackFruits presenter]

**Fork Repository (2 min):**
> "Great! Now fork this repository to your own account. You'll use your peers' summaries from Discussion 1 as test data for your agent."

---

## Phase 2: Agent Design (~60 min)

### Key Facilitator Moments:

**Kickoff (5 min):**
> "You've now experienced:
> - Writing under constraints
> - Identifying quality
> - Giving feedback
> - Using a rubric
>
> Time to build an agent that does this! In GitHub Copilot Chat: click the + button → Instructions → Configure Instructions → + New Instruction file. Name it with your group number: group1-feedback-agent.md, group2-feedback-agent.md, etc. Write rules for how your agent should give feedback."

**Design questions to pose:**
- Should your agent score first or guide through questions?
- Focus on one dimension or all five?
- Correct errors or ask reflective questions?
- Sound like a teacher, peer, or coach?

**Mid-phase check-in (30 min mark):**
> "Teams: have you tested your agent with Copilot Chat yet? Try it on your own summary from Phase 1!"

---

## Phase 3: Cross-Testing (~25 min)

### Assignments:
Prepare team rotation (e.g., Team A tests Team B, Team B tests Team C, Team C tests Team A)

**Kickoff:**
> "Clone the team assigned to you. Test their agent on YOUR summary from Phase 1. Submit feedback via GitHub Issues using the template."

---

## Phase 4: Iteration (~30 min)

**Kickoff:**
> "Check your Issues tab. What did other teams notice? Pick 1-3 changes to make. Update your agent and test again."

---

## Phase 5: Showcase & Vote (~25 min)

### Setup:
- Teams at stations around room
- Laptops open to their agent + Copilot Chat
- Optional: Create GitHub Discussion poll for voting, or use show of hands

**Gallery walk (15 min):**
> "Visit every station. Submit your summary to their agent. Ask about their design choices."

**Vote (10 min):**
> "Vote for the most effective agent (not your own). Consider: usefulness, specificity, rubric use, tone, creativity."

**Closing:**
> "Winner: [Team Name]! Brief demo of their approach. Thank you all—your designs will help us understand what makes AI feedback truly useful."

---

## Post-Event

- Export all GitHub repositories (for research)
- Send thank-you email with research summary timeline
- Share winning agent as inspiration for future participants
