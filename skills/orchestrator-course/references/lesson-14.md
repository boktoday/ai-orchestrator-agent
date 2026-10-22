# Lesson 14 - Failure drills
*Guardrails · about 45 minutes · artefact: `guardrails/drills.md`*

## What you are making
Three deliberate failures, each caught, each written up: a wrong answer that sounded right, a broken deploy, and a secret in the wrong place.

## Why it matters
You will not spot a failure you have never seen. These drills are cheap inoculations: cause the failure on purpose, in a place where nothing is at stake, and the same failure becomes visible at work.

## The demo
The coach breaks its own figure three ways: it removes a file the page needs and shows the blank screen; it deploys a page with a typo in the address; it puts a fake key in a file and shows what a scanner would say. For each it names the symptom, the cause and the check that catches it.

## Your turn
Run the three drills on your own work and record each in `guardrails/drills.md`:
1. **The confident wrong answer.** Ask something with a checkable fact, catch it, and record the source that proved it wrong.
2. **The broken deploy.** Break a link or a file on purpose, see what a visitor would see, fix it.
3. **The leak.** Put a fake secret in a file, run a search for it, and record what you found and where it should have lived.

## The check
1. All three drills recorded with symptom, cause and check.
2. Each failure was actually caused, not imagined.
3. The fix is written next to it.
4. Nothing real was harmed: no live client site, no real key.

Failure signs: write-ups of failures the student read about rather than caused.

## Sealed when
`guardrails/drills.md` is complete and the student names the failure they are most likely to repeat.
