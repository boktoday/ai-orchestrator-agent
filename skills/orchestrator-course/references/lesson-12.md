# Lesson 12 - Clocks: what a cronjob is
*Connect and automate · about 45 minutes · artefact: `automate/<job>/` with a run log*

## What you are making
One scheduled job of your own, with a schedule you can explain, one successful run and one failed run recorded.

## Why it matters
A scheduled job is the difference between work you remember to do and work that happens. Cron is the old, plain, powerful grammar underneath nearly every scheduled thing, and it is five fields you can learn in ten minutes. What takes longer is learning to make a job safe: it must survive a run where the input is missing, say when it failed, and never do the same thing twice by accident.

## The demo
The coach writes a five-field schedule and reads it aloud (minute, hour, day of month, month, day of week), then sets a job that runs a minute from now, watches it fire, and shows the run log. Then it breaks the job on purpose (a missing input file) and shows what a silent failure looks like, then adds the two lines that make it report instead of dying quietly.

## Your turn
1. Choose a small job worth running on a clock: a morning summary, a weekly tidy, a reminder.
2. Put it in `automate/<job>/` with the script, a README stating the schedule in words and in five fields, and the timezone named.
3. Run it once by hand and once on the schedule. Save both runs in `run-log.md`: time, input, output, duration.
4. Break it deliberately: remove an input, run again, and record how it failed and what you changed so it reports next time.

## The check
1. The schedule is written in five fields and in plain English, with the timezone named.
2. Two real runs logged, one by hand and one on time.
3. One deliberate failure recorded, with the fix that makes it speak rather than die.
4. The job is safe to run twice: it does not duplicate its output or double-send.

## Sealed when
The folder holds script, README and run log, the job fires on its own, and the student can say what happens if the input is missing.
