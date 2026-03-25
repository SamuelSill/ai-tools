---
name: fix-review-feedback
description: Use when the user has received review comments on their PR and needs help addressing them. Goes through each comment interactively, validating and suggesting fixes.
---

# Viewing PR comments and reviews

To view comments and reviews on a PR, use separate commands (not chained with `;`) so they get auto-approved:

- PR reviews: `gh pr view <number> --json reviews --jq '.reviews[] | "**\(.author.login)** (\(.state)):\n\(.body)\n---"'`
- Inline review comments: `gh api repos/{owner}/{repo}/pulls/<number>/comments --jq '.[] | "**\(.user.login)** on \(.path):\n\(.body)\n---"'`
- PR conversation comments: `gh api repos/{owner}/{repo}/issues/<number>/comments --jq '.[] | "**\(.user.login)**:\n\(.body)\n---"'`

# Fix Review Feedback

**STOP Before you open the user's PR, if the user asks you to fix their branch's review comments, you MUST:**

Go over each of the comments one by one, and for each one:
Determine if the comment is valid and describes a real issue in the code:
- If it's not valid, explain why. Ask for confirmation to reply to the reviewer on behalf of the user.
- If it's valid, determine a fix to the comment and suggest it to the user.

Wait for the user's confirmation before moving to the next comment - they might modify and push fixes before proceeding.

Note that some fixes may automatically fix the other comments - don't skip them.
Instead, explain why they were already resolved, and wait for confirmation.

* If a comment specifies multiple different issues, split the comment to those issues and do the above process for each of them.
