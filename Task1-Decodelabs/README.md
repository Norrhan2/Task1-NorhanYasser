# Project 1: Rule-Based AI Chatbot 🤖

**DecodeLabs Industrial Training Kit — Batch 2026**

---

## What This Is

A rule-based AI chatbot built in Python. It simulates conversation using deterministic logic — no machine learning, no APIs. Every response is 100% predictable and traceable.

This is the foundation of all AI systems: before you can manage probabilistic outputs (like LLMs), you must master building the **control layer** on top of them.

---

## How It Works — The IPO Model

```
USER INPUT  →  SANITIZE  →  DICTIONARY LOOKUP  →  PRINT RESPONSE
                              (if no match → fallback)
```

| Phase | What Happens |
|-------|-------------|
| **Input** | `raw_input.lower().strip()` — normalizes "HELLO", "Hello ", "hello" → all become `"hello"` |
| **Process** | `responses.get(key, fallback)` — O(1) dictionary lookup, not a fragile if-elif ladder |
| **Output** | Response printed, loop continues until `exit` / `bye` / `quit` |

---

## Why a Dictionary, Not If-Elif?

| Approach | Complexity | Maintainability |
|----------|-----------|-----------------|
| If-Elif ladder | O(n) — slows down as rules grow | Hard — every new rule = new elif |
| Dictionary `.get()` | **O(1) always** | Easy — just add a new key-value pair |

---

## Running It

```bash
python chatbot.py
```

Sample session:
```
You: hello
Bot: Hello! I'm DecoBot 🤖 How can I help you today?

You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs! 🐛

You: exit
Bot: Goodbye! Keep building great things. 👋
```

---

## Key Concepts Demonstrated

- **Continuous loop** — `while True` keeps the bot alive
- **Input sanitization** — handles case and whitespace
- **Knowledge base** — dictionary with 5+ intents
- **Fallback response** — handles unknown inputs gracefully
- **Exit strategy** — clean `break` on exit commands

---

## Project Requirements Checklist

- [x] Handle greetings and exit commands
- [x] Use if-else / dictionary logic for responses
- [x] Run in a continuous loop
- [x] Input sanitization (case + whitespace)
- [x] Knowledge base with 5+ intents
- [x] Default fallback for unknown inputs
- [x] Clean exit command

---

*DecodeLabs | Powered by pure Python logic*
