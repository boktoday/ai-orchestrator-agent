# Lesson 10 - What an API is, and what it is not
*Connect and automate · about 50 minutes · artefact: `connect/api-log.md`*

## What you are making
A log of two real API calls you made yourself, request and response, and a plain-English note on what each one proved.

## Why it matters
An API is how one program asks another to do something, and almost everything you will automate rests on it. It is not magic and it is not a chat: it is an address, a permission and a shaped answer. Once you can read a request and a response, the whole automation layer stops being mysterious.

## The demo
The coach opens a terminal and makes two read-only calls in front of the student: a public endpoint that needs no key, and a Gmail read through a managed connection. For each it names the four parts out loud: the address (endpoint), the permission (the key or the connection), the request (a GET, with parameters), and the answer (a status code plus JSON). It then shows what a 401 and a 429 look like, because the errors teach faster than the successes.

## Your turn
1. Make one call to a public API with no key, and one read-only call through a managed connection to your own Gmail or Calendar. Read-only only: list, do not send.
2. Write `connect/api-log.md` with both calls: the endpoint, the permission used, the status code, and the first twenty lines of the response, trimmed.
3. Under each, one sentence: what this call proves you can now do.
4. Add an error section: force one bad call (wrong path or no key) and record the status and message.

## The check
1. Two real calls, with real status codes, not paraphrased.
2. No secret pasted into the file: the log names where the key lives, never its value.
3. The error section shows one failure and what caused it.
4. The student can say which part of the call was the permission and which was the address.

Failure signs: a log made of documentation quotes, or a key visible in the file.

## Sealed when
`connect/api-log.md` holds two calls, one failure, and no secret, and the student explains the four parts without notes.
