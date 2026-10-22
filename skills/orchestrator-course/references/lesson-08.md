# Lesson 8 - An agent that does a chore
*Build · about 60 minutes · artefact: `build/chore/` with one run log*

## What you are making
A small repeatable workflow that does a real chore for you, with one guardrail, and a log of a real run.

## Why it matters
Using an AI on demand is a conversation. Directing one on a schedule is a system. The difference is what makes you an orchestrator rather than a user: the work happens without you starting it.

## The demo
The coach writes a small script that gathers three inputs and produces a weekly one page brief, with a guardrail: nothing is sent anywhere without the human reading it first. It runs once, prints its output, and shows the log line it wrote.

## Your turn
Create `build/chore/` containing:
1. A script or a prompt that does one chore you actually have.
2. A README with the inputs, the output, and the guardrail.
3. `run-log.md` with one real run: date, input, output, what you changed.

## The check
1. The script runs from a clean terminal with one command.
2. The guardrail is real: a human step before anything leaves the machine.
3. The log records a real run, not a rehearsal.
4. No credentials in the folder; the README says where the key lives.

Failure signs: a workflow that only exists as a chat transcript, or a guardrail that is a comment rather than a step.

## Sealed when
A real run is logged, the guardrail is demonstrated, and the folder is committed or archived.
