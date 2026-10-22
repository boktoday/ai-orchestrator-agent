# Lesson 11 - Connected tools and webhooks
*Connect and automate · about 50 minutes · artefact: `connect/event-log.md`*

## What you are making
One connected service and one real event captured, with the payload saved and explained.

## Why it matters
Two ways to learn that something happened: go and ask on a timer (polling), or be told the moment it happens (a webhook). Webhooks are why automation feels instant, and why an agent can react to an email, a form or a payment without you sitting there. Managed connections are how you get in without handling anyone password.

## The demo
The coach shows a connection to Gmail and to a calendar: what the authorisation screen actually grants, and why it is safer than pasting a password into a script. Then it creates a trigger that fires on an event and points it at a test destination, sends the event, and reads the delivered payload aloud, naming the field that says what happened and the field that says who it was.

## Your turn
1. Connect one service you actually use: Gmail, Calendar, or an SMS gateway.
2. Create one trigger, or point a webhook at a capture address you can read, and cause the event: send yourself one email, or create one calendar entry.
3. Save the delivered payload in `connect/event-log.md`: the event type, the two or three fields that matter, and the fields you can ignore.
4. Write one sentence: what you would now build if this event arrived every morning.

## The check
1. A real event captured, with its payload, not a screenshot of documentation.
2. The log names the connection used and the scope granted.
3. Two fields identified as meaningful, and one explained as noise.
4. Nothing destructive was wired: no trigger that sends, deletes or pays without a human step.

## Sealed when
`connect/event-log.md` holds a real payload and the student can say what pushes, what polls, and why the difference matters.
