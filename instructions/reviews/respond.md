# Fix Review Feedback

**STOP Before you open the user's PR, if the user asks you to fix their branch's review comments, you MUST:**

Go over each of the comments one by one, and for each one:
* **IMPORTANT:** If the user has already addressed it via a reply or a reaction, skip the comment and move on to the next one.

If it wasn't addressed yet - determine if the comment is valid and describes a real issue in the code:
* If it's not valid, explain why. Ask for confirmation to reply to the reviewer on behalf of the user.
* If it's valid, determine a fix to the comment and suggest it to the user.
  When you're done, ask for confirmation to reply with a 👍 reaction to the comment, indicating that it's fixed.

Wait for the user's confirmation before moving to the next comment - they might modify and push fixes before proceeding.

Note that some fixes may automatically fix the other comments - don't skip them.
Instead, explain why they were already resolved, and wait for confirmation.

* If a comment specifies multiple different issues, split the comment to those issues and do the above process for each of them.

**When you're done going over all the comments:**

If any changes were made, make sure to verify them via building/running tests.
If there are no relevant tests - give instructions to the user on how to verify the changes.
