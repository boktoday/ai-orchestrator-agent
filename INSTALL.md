# Installing the AI Orchestrator Agent

## 1. Install Hermes Agent

Follow the official guide at https://hermes-agent.nousresearch.com/docs and connect the chat app you already use. Telegram is recommended: it is private and works on any phone.

## 2. Get a model key

Any provider Hermes supports will do. A cheap one is plenty for the whole course:
OpenRouter (free tiers work), DeepSeek, or a local model through Ollama. Put the key in your Hermes `.env`.

## 3. Copy the profile

- `skills/` into your Hermes profile `skills/` folder
- `SOUL.md` alongside it, or merge its principles into your profile instructions
- `config.yaml` is an example; merge what you need

## 4. Make your work folder

```
python skills/orchestrator-course/scripts/start_course.py
```

This creates `~/ai-orchestrator` with `progress.json`, `position/`, `prompts/`, `build/`, `guardrails/` and the templates.

## 5. Start

Open your chat and say:

> Start my first lesson.

The coach reads your progress file and runs lesson 1. Every later session starts the same way: it looks at your progress and picks up where you stopped.

## What you need

A laptop, a browser, and about 30 to 50 minutes per lesson. Three lessons make a module. Fifteen lessons is five sittings if you are quick, nine or ten if you work properly.
