---
name: review-pr
description: Use when the user wants to review another person's GitHub PR. Provides structured analysis with JIRA context, module onboarding, and a final problem summary table.
---

# Viewing PR comments and reviews

To view comments and reviews on a PR, use separate commands (not chained with `;`) so they get auto-approved:

- PR reviews: `gh pr view <number> --json reviews --jq '.reviews[] | "**\(.author.login)** (\(.state)):\n\(.body)\n---"'`
- Inline review comments: `gh api repos/{owner}/{repo}/pulls/<number>/comments --jq '.[] | "**\(.user.login)** on \(.path):\n\(.body)\n---"'`
- PR conversation comments: `gh api repos/{owner}/{repo}/issues/<number>/comments --jq '.[] | "**\(.user.login)**:\n\(.body)\n---"'`

# Review PR

**STOP Before you review ANY change, if the user asks you to review another person's PR, you MUST:**

* Find the relevant JIRA tickets this PR aims to resolve, and explain them to the user - verify that they understand.
* If the PR introduces nontrivial modifications to island modules, for each of those modules -
  Ask the user if they need to be onboarded on the module. If so, dive deep into the module (before the changes) and understand its role in the project and what it aims to achieve.
  Then explain the module simply:
  * Where in the project is it used?
  * What is its purpose?
  * Broadly, how is it implemented? What's the main idea behind the implementation/algorithm?
  * If there's any interface between this module and another one modified in the PR, elaborate on it.
* Once the user has a good understanding of the code before the changes, start reviewing them. Go over each commit in the PR, and for each of them:
  * Explain briefly what it aims to solve.
  * Explain any nontrivial changes - break down new modules, look at modifications in general and explain what they aim to achieve, etc.
  * Try to find potential bugs that might crash the code.
  * Look for places where the code might be inefficient unnecessarily.
  * If the code modifies web interfaces that other projects rely on (for example extension API), verify backwards compatibility.
  * Verify that the code is readable and clean.
  * Review the commit/commit message - does the commit make sense as a standalone addition to the project? Does the message describe the change well enough?
  For any problem that you find, tell the user about it. If they agree - keep note of the problem, otherwise forget about it.

* When you're done, ask for confirmation to show a full table of the problems with the following columns (sorted by category):
  * Code location
  * Category - Bug/Crash/Readability/etc.
  * Comment - a suggested comment to post on the PR. Try to make it short and simple
  * Fix Suggestion - only when the fix to the problem is really small, otherwise keep empty.
