---
name: review
description: Use when the user wants to review another person's GitHub PR. Provides structured analysis with JIRA context, module onboarding, and a final problem summary table.
---

**STOP Before you reply to any comment on a PR:**

* Always prefix the reply with an expandable "Replied via" note using this format:
  ```
  <details><summary>Replied via [NAME OF AGENT]</summary>
  <sub><i>This reply was written using [NAME OF AGENT] and approved by [[THE USER'S USERNAME]] before posting.</i></sub>
  </details>
  ```
* Always ask for confirmation before posting the reply.
* Never resolve the comments yourself.

# Viewing PR comments and reviews

To view comments and reviews on a PR, use separate commands (not chained with `;`) so they get auto-approved.

For GitHub CLI, use the following:

- PR reviews: `gh pr view <number> --json reviews --jq '.reviews[] | "**\(.author.login)** (\(.state)):\n\(.body)\n---"'`
- Inline review comments: `gh api repos/{owner}/{repo}/pulls/<number>/comments --jq '.[] | "**\(.user.login)** on \(.path):\n\(.body)\n---"'`
- PR conversation comments: `gh api repos/{owner}/{repo}/issues/<number>/comments --jq '.[] | "**\(.user.login)**:\n\(.body)\n---"'`

* When showing PR comments/replies to the user, if the comment is about specific lines, **ALWAYS** show the user the lines in question for context.

# Review PR

**STOP Before you review ANY change, if the user asks you to review another person's PR, you MUST:**

Go through the following steps one by one.
**IMPORTANT:** Wait for user confirmation before moving between these steps.

1. **Read through the Project's Instructions**

Before you do anything, make sure you've read the project's guidelines, so that you understand how the project works,
what are the best practices, and what to look for in a review.

2. **Explain the Issue that Led to the Change**

Find the relevant issue tickets this PR aims to resolve, and explain them to the user - verify that they understand.

3. **Onboard the User Step by Step on the Relevant Modules**

One by one, for each one of the modules that has nontrivial modifications in the PR, ask the user if they need to be onboarded on the module.
If so, dive deep into the module (before the changes) and understand its role in the project and what it aims to achieve.
Then explain the module simply:
* Where in the project is it used?
* What is its purpose?
* Broadly, how is it implemented? What's the main idea behind the implementation/algorithm?
* If there's any interface between this module and another one modified in the PR, elaborate on it.

Wait for user confirmation before proceeding to the review.

4. **Review the PR Silently**

Without talking to the user yet, go over each commit in the PR one by one, and for each commit:
* Understand what it aims to solve.
* Understand any nontrivial changes - break down new modules, look at modifications in general and understand what they aim to achieve, etc.
* Try to find potential bugs that might crash the code.
* Look for places where the code might be inefficient unnecessarily.
* If the code modifies web interfaces that other projects rely on (for example extension API), verify backwards compatibility.
* Verify that the code is readable and clean.
* Review the commit/commit message - does the commit make sense as a standalone addition to the project? Does the message describe the change well enough?

Keep track of any problem that you find in this part, do not discuss about them with the user yet.

5. **Discuss Each Problem with the User**

Go over each problem you found in the previous step sorted by the commit order, and one by one:
* Explain the problem simply to the user.
* Ask the user if they agree with the problem. If so, keep note of it. Otherwise forget about the problem.
**IMPORTANT:** Wait for user confirmation before moving to the next problem.

When you're done discussing all of the problems, proceed to the next step.

6. **Ask the User for Problems**

Ask the user if they want to dicuss any issues in the PR. For each issue, check if it's actually valid:
* If it's valid, keep note of it.
* If it isn't, tell the user why you think it's not valid, and ask if the user still wants to keep it.

When you're done discussing all of the user's problems, proceed to the summary.

7. **Summarize the Problems**

Ask for confirmation to show a full table of the problems with the following columns (sorted by category):
* Code location
* Category - Bug/Crash/Readability/etc.
* Comment - a suggested comment to post on the PR. Try to make it short and simple
* Fix Suggestion - only when the fix to the problem is really small, otherwise keep empty.

8. **Suggest Help with Replying to the Review**

For each problem:
* Find the most fitting location in the review to comment.
* Write a simple and readable comment describing the problem. Keep it short. If you have a short fix suggestion, add it to the comment.
  Iterate with the user on the comment until they are content with it, and when you're done, comment it on the PR.
* If the problem is relevant to many code locations, ask for confirmation to comment a reference comment on all of them, that redirects
  the PR assignee to look at one comment that explains the issue.
