# Viewing PR comments and reviews

To view comments and reviews on a PR, use separate commands (not chained with `;`) so they get auto-approved:

- PR reviews: `gh pr view <number> --json reviews --jq '.reviews[] | "**\(.author.login)** (\(.state)):\n\(.body)\n---"'`
- Inline review comments: `gh api repos/{owner}/{repo}/pulls/<number>/comments --jq '.[] | "**\(.user.login)** on \(.path):\n\(.body)\n---"'`
- PR conversation comments: `gh api repos/{owner}/{repo}/issues/<number>/comments --jq '.[] | "**\(.user.login)**:\n\(.body)\n---"'`
