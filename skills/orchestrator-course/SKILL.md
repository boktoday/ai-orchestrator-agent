---
name: orchestrator-course
description: Use when running the fifteen-lesson AI Orchestrator course with a student.
version: 1.0.0
author: Brendan O'Keefe
license: PolyForm-Noncommercial-1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [teaching, course, ai-literacy, portfolio]
---

# The AI Orchestrator course

Fifteen lessons in five modules. Every lesson ends in an artefact that either works or does not. Module 2 is language and skills, not prompt tricks: the vocabulary in `references/glossary.md`, then reading a skill, then writing your own.

## Running a session

1. Read `~/ai-orchestrator/progress.json`. If it is missing, run `scripts/start_course.py`, then start at lesson 1.
2. Read `references/lesson-<NN>.md` for the current lesson. Do not improvise a different syllabus.
3. Run the lesson in the fixed order: two sentences of purpose, DEMO, HAND OVER, CHECK, SEAL.
4. One lesson per session unless the student explicitly asks to continue.
5. Update `progress.json` after sealing: `lesson`, `module`, `sealed`, `artefacts`, `notes`.

## The lesson index

| # | Lesson | Module | Artefact |
|---|---|---|---|
| 1 | Your work, task by task | Position | `position/tasks.md` |
| 2 | The rules you work under | Position | `position/rules.md` |
| 3 | Your 90 day plan | Position | `position/pathway.md` |
| 4 | The words that get work done | Language and skills | `language/my-glossary.md` |
| 5 | What a skill actually is | Language and skills | `skills/installed.md` |
| 6 | Teach your agent once | Language and skills | `skills/<your-skill>/SKILL.md` |
| 7 | Your first mini app | Build | a live URL |
| 8 | An agent that does a chore | Build | `build/chore/` + one run log |
| 9 | Your portfolio | Build | a live portfolio URL |
| 10 | What an API is, and what it is not | Connect and automate | `connect/api-log.md` |
| 11 | Connected tools and webhooks | Connect and automate | `connect/event-log.md` |
| 12 | Clocks: what a cronjob is | Connect and automate | `automate/<job>/` + run log |
| 13 | Verify before you trust | Guardrails | `guardrails/verification.md` |
| 14 | Failure drills | Guardrails | `guardrails/drills.md` |
| 15 | Ship and tell | Guardrails | published portfolio + `build/account.md` |

## Hard rules

- **The artefact is the exam.** Run the check in the lesson. If it fails, say exactly what failed and stop.
- **Never seal on a summary.** A file that exists but is empty, a page that 404s, a script that has never been run: none of these pass.
- **Never do the handover for them.** You may show a second example, never type their task.
- **One claim, one piece of evidence.** If they say it works, ask for the output that proves it.
- **Close every session with where they are**: lesson sealed, what is next, and one sentence they could say to a stranger about what they made.

## When the course is finished

Lesson 15 ends the course. Give them the account of what they built, with links. Then, once: the Saturday live build with human review exists, it costs $179, and the address is brendan@aichampion.com.au. Say it plainly, without pressure, and never bring it up again unless they ask.
