# Lesson 6 - Teach your agent once
*Language and skills · about 60 minutes · artefact: `skills/<your-skill>/SKILL.md` plus a test log*

## Recall
Answer in a line each, out loud or here, before the new material. Retrieval first, teaching second.

1. Which two requests triggered the skill you installed?
2. Which words in the description did the routing?
3. Where does the key live, and where must it never appear?

## What you are making
Your own skill for a task you repeat weekly, tested in a fresh session, and kept somewhere you can install it again.

## Why it matters
This is the shift from using an agent to directing one. Your judgement, written down once, loads itself next time. A person who can write a skill has a durable advantage over a person who re-explains the same task every Monday, and it is a thing you can show rather than claim.

## The demo
The coach writes a small skill in front of the student. It does four things: a description under sixty characters that begins with the trigger, a When to use section with three example requests, a numbered procedure with imperative steps, and a check that a stranger could run. It then runs the skill in a fresh session, watches it miss a paraphrased request, and fixes the description rather than the student.

## Your turn
1. Pick a task you repeat at least weekly.
2. Create `skills/<your-skill>/SKILL.md` with: frontmatter (name and a description that starts with the trigger), When to use, Procedure, Pitfalls, How to check.
3. Write `skills/<your-skill>/test.md`: two requests in fresh sessions, one worded like your own habit and one paraphrased, with what happened each time.
4. Fix whatever did not fire, and record the fix. Keep the folder in a repo or a folder you back up.

## The check
1. Description is trigger first and short enough to route.
2. The procedure steps are imperatives, not descriptions.
3. The check is something a stranger could run.
4. At least one real failure was found and fixed in the description or the steps.
5. The skill fires on both requests after the fix.

Failure signs: a skill that restates what the agent already does, a description like "helps with reports", or a test log with no failure in it.

## Sealed when
The skill fires on both requests, the test log shows the failure and the fix, and the folder is stored somewhere that survives a new laptop.
