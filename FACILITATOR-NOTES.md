# Facilitator Notes

**Event:** Can AI Give Good Feedback? Build One and Find Out  
**Duration:** 3 hours (18:00-21:00)  
**Date:** June 17, 2026  
**Venue:** FeedbackFruits, Amsterdam

---

## Event Overview

**Participant Resources:**
- **README.md** — Landing page with agenda
- **phase1-orientation.md** through **phase5-showcase.md** — Step-by-step guides for each phase
- **CONSENT.md** — Research participation consent form

**Facilitator Materials:**
- This document (FACILITATOR-NOTES.md)
- Pre-created GitHub Discussions
- Team assignments
- Cross-testing rotation plan

---

## Pre-Event Setup (Complete Before 18:00)

### 1-2 Days Before Event: Email Participants (Optional)

**Optional:** Send participants the **[SETUP.md](SETUP.md)** link to set up in advance. However, Phase 1 Step 6 includes dedicated time (12 min) for setup, so this is not required.

> **Subject:** Get Ready for "Can AI Give Good Feedback?" Hackathon
>
> Hi everyone,
>
> Thanks for registering for our hackathon on June 17!
>
> You'll need a **GitHub account** to participate. If you don't have one, please create one at https://github.com/signup before arriving.
>
> **Optional preparation:** To save time during the event, you can install VS Code, Git, and GitHub Copilot in advance using our [Setup Guide](https://github.com/madiepev/feedback-agent-hackathon/blob/main/SETUP.md). If you don't, we have dedicated setup time built into Phase 1 (Step 6).
>
> See you Tuesday at 18:00!
>
> Mary-Jo & Bas

### Day of Event: GitHub Discussions Preparation

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

**Discussion 2: Which Agent Was Most Effective?**
- **Title:** Which agent was most effective?
- **Category:** General
- **Body:**
```markdown
After community testing, reply with:

1. Which team's agent you found most effective
2. Why it was effective, with specific examples from the feedback you received

Please do not vote for your own team's agent.
```

### Materials Checklist
- [ ] Discussion 1 (Share Your Summary) created and pinned
- [ ] Discussion 2 (Which agent was most effective?) created for Phase 5
- [ ] Consent forms printed (CONSENT.md)
- [ ] Participant ID stickers or cards (P001, P002, etc.)
- [ ] Projector/screen for displaying discussion responses live
- [ ] (Optional) Send SETUP.md link to participants 1-2 days before event
- [ ] Team assignments prepared (6 teams of 3 people for 18 participants)
- [ ] Cross-testing assignments ready (which team tests which)

---

## Event Timeline (18:00-21:00)

### **17:45-18:00 — Arrival & Setup (15 min)**
- Participants arrive
- Distribute consent forms (CONSENT.md)
- Assign participant IDs to those who consent
- **Quick check:** Does everyone have a GitHub account?
  - If not, help them create one at github.com/signup
- Form teams (6 teams of 3 people)

**Note:** VS Code/Git/Copilot setup happens in Phase 1 Step 6 (12 min allocated)

---

### **18:00-18:15 — Welcome & FeedbackFruits Presentation (15 min)**

**Timeline:**
- **18:00-18:05** (5 min) — Welcome & event overview
- **18:05-18:15** (10 min) — FeedbackFruits presentation

**Facilitator Script:**

**Welcome (18:00-18:05):**
> "Welcome to 'Can AI Give Good Feedback?' I'm [Name] from VU Amsterdam. Today you'll design AI feedback agents for science writing.
>
> This is also a research study. If you signed a consent form, your agent designs and feedback will help us understand what students value in AI feedback. Participation is voluntary.
>
> Here's how tonight works: You'll write summaries, learn a rubric, design AI agents, test each other's work, and share what made certain approaches effective.
>
> But first, let's hear from our host, FeedbackFruits, about why educational feedback matters."

**FeedbackFruits Presentation (18:05-18:15):**
> [Hand off to FeedbackFruits presenter for 10 minutes]

---

### **18:15-19:05 — Phase 1: Orientation & Elicitation (50 min)**

**Guide:** Participants follow [phase1-orientation.md](phase1-orientation.md)

**Timeline:**
- **18:15-18:30** (15 min) — Read article & write summaries
- **18:30-18:35** (5 min) — Share reactions to summaries
- **18:35-18:45** (10 min) — Group discussion: What makes good feedback?
- **18:45-18:53** (8 min) — Introduce the Universal Science Writing Rubric
- **18:53-19:05** (12 min) — Fork repository & setup

### Facilitator Script:

**Introduction to Phase 1 (18:15):**
> "Now let's experience the task ourselves. Navigate to the Discussions tab—I've pinned 'Phase 1: Share Your Summary' at the top. Read the Mars article (assets/article.md), then write a 50-100 word summary and post it as a comment. You have 15 minutes. Go!"

**After posting period (18:30-18:35):**
> "Now refresh the discussion. Read your peers' summaries. React with 👍 to the ones you think are strongest. Trust your instincts—we'll analyze why later."
>
> [Give 2-3 minutes for reactions, then refresh and sort by reactions]

**Quality & Improvement Discussion (18:35-18:45):**
> "Let's look at the summaries with the most reactions. [Read top 2-3 aloud]. What made these effective? Call out specific features."
> 
> [Collect responses verbally, write themes on board/screen: accuracy, clarity, completeness, evidence, etc.]
> 
> "Notice these patterns—you're already experts at recognizing quality!"
>
> "Now look at some other summaries. What could they improve? What's missing or unclear?"
>
> [Collect responses, highlight themes: vague language, missing evidence, too much background, etc.]
>
> "Great—you've just done what feedback agents need to do: identify quality AND explain how to improve."

**Rubric Introduction (18:45-18:53):**
> "Your intuitions align with research. Let me introduce the Universal Science Writing Rubric—it formalizes the criteria you just discovered."
>
> [Walk through 5 dimensions: Content Accuracy, Interpretation, Audience, Organization, Writing Quality]
>
> "This rubric is your agent's foundation. Your job is to decide HOW it should use these criteria to help students."

**Fork & Setup Repository (18:53-19:05):**
> "Great! Now it's time to set up your development environment. You'll fork this repository and install the tools you need to build your AI agent.
>
> **Step 1:** Fork this repository to your own GitHub account - click the Fork button at the top.
>
> **Step 2:** Follow the setup guide to install VS Code, Git, and GitHub Copilot if you haven't already. The link is in phase1-orientation.md Step 6."

**Facilitator Actions During This Time:**
- Circulate and help with setup issues
- Direct participants to [SETUP.md](SETUP.md) for detailed instructions
- Help with common issues:
  - Installing VS Code/Git if not already installed
  - Installing GitHub Copilot extension in VS Code
  - Signing into GitHub in VS Code
  - Cloning their forked repository
- For those who can't get VS Code working: explain they can create agent files via GitHub web but won't test until Phase 3
- **Check at 19:00:** Is everyone ready to start Phase 2? Extend by 5 min if needed.

---

### **19:05-19:50 — Phase 2: Agent Design (45 min)**

**Guide:** Participants follow [phase2-agent-design.md](phase2-agent-design.md)

**Timeline:**
- **19:05-19:15** (10 min) — Design strategy discussion
- **19:15-19:35** (20 min) — Create instruction file
- **19:35-19:45** (10 min) — Test agent
- **19:45-19:50** (5 min) — Commit changes

### Key Facilitator Moments:

**Kickoff (19:05):**
> "You've now experienced writing, identifying quality, giving feedback, and using a rubric. Time to build an agent that does this!
>
> In GitHub Copilot Chat: click the + button → Instructions → Configure Instructions → + New Instruction file. Name it with your group number: group1-feedback-agent.md, group2-feedback-agent.md, etc.
>
> Key design questions to discuss as a team:
> - Should your agent score first or guide through questions?
> - Focus on one rubric dimension or all five?
> - Correct errors directly or ask reflective questions?
> - Sound like a teacher, peer, or coach?
> - How specific? Quote the text? Give examples?
>
> You have 45 minutes. Go!"

**Mid-phase Check-in (19:25):**
> "Teams: have you tested your agent with Copilot Chat yet? Try it on your own summary from Phase 1!"

**Final Check (19:45):**
> "Make sure you've committed your instruction file to GitHub!"

---

### **19:50-20:15 — Phase 3: Cross-Testing (25 min)**

**Guide:** Participants follow [phase3-cross-testing.md](phase3-cross-testing.md)

**Timeline:**
- **19:50-19:52** (2 min) — Assignments announced
- **19:52-20:02** (10 min) — Test assigned agent
- **20:02-20:15** (13 min) — Submit feedback via GitHub Issue

### Assignments:
Prepare team rotation beforehand (e.g., Team 1 tests Team 2, Team 2 tests Team 3, etc.)

**Kickoff (19:50):**
> "Team assignments:
> - Team 1, test Team 2's agent
> - Team 2, test Team 3's agent
> [etc.]
>
> Navigate to their repository, use their agent on YOUR summary from Phase 1, then submit feedback via GitHub Issues using the 'Agent Feedback (Phase 3)' template.
>
> The form asks you to rate the agent on 5 criteria (Understandability, Specificity, Validity, Actionability, Affective Quality) using a 5-point scale and provide evidence for each rating. You'll also give an overall rating and feedback. You have 25 minutes!"

---

### **20:15-20:40 — Phase 4: Iteration (25 min)**

**Guide:** Participants follow [phase4-iteration.md](phase4-iteration.md)

**Timeline:**
- **20:15-20:25** (10 min) — Review feedback received
- **20:25-20:37** (12 min) — Revise agent
- **20:37-20:40** (3 min) — Commit v2

**Kickoff (20:15):**
> "Check the Issues tab in the main repository. Find the feedback about YOUR agent. What did other teams notice? Pick 1-3 changes to make based on their ratings and evidence. Update your agent and test again. You have 25 minutes!"

**Mid-phase (20:30):**
> "10 minutes left! Make sure you test your improved version!"

---

### **20:40-21:00 — Phase 5: Community Testing & Reflection (20 min)**

**Guide:** Participants follow [phase5-showcase.md](phase5-showcase.md)

**Timeline:**
- **20:40-20:54** (14 min) — Open testing
- **20:54-21:00** (6 min) — Discussion voting & debrief

### Setup:
- GitHub Discussion created: "Which agent was most effective?"
- All teams' repositories accessible

**Open Testing (20:40-20:54):**
> "For the next 14 minutes, test as many agents as you'd like! Navigate to different teams' repositories, use their agents with YOUR summary from Phase 1. Note what works well and what makes certain approaches more effective than others."

**Discussion Voting (20:54-21:00):**
> "Head to the Discussions tab and find 'Which agent was most effective?' 
>
> Reply with:
> - Which team's agent you found most effective (not your own)
> - Why it was effective — be specific!
>
> What features made it stand out? Was it the specificity? The tone? How it used the rubric? Give us details!"

[Allow 3-4 minutes for responses]

**Closing (20:57-21:00):**
> "Let's look at the responses... [Read 2-3 aloud, highlighting different effective features]
>
> Notice how different teams valued different features? Some prioritized specificity, others tone, others structure. That's exactly what this research explores!
>
> Thank you all! Your designs and reflections will help us understand what makes AI feedback truly useful. If you consented to research, we'll analyze your agents and share findings at ICERI2026.
>
> Keep experimenting with GitHub Copilot instructions—this is a powerful way to customize AI behavior!"

---

## Post-Event Tasks

**Immediately After:**
- [ ] Collect all signed consent forms
- [ ] Assign participant IDs to consent forms
- [ ] Create secure storage for consent forms (10 year retention)

**Within 1 Week:**
- [ ] Export all GitHub repositories (participant forks + main repo with Issues)
- [ ] Anonymize data: Replace GitHub usernames with participant IDs
- [ ] Store research data securely
- [ ] Send thank-you message to participants

**Within 1 Month:**
- [ ] Analyze agent designs and feedback patterns
- [ ] Prepare findings for ICERI2026 presentation

**After Publication:**
- [ ] Share winning agent design as example (anonymized)
- [ ] Make anonymized dataset available for research community (optional)
