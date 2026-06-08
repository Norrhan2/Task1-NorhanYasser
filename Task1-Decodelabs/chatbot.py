"""
Project 1: Rule-Based AI Chatbot

Architecture: IPO Model (Input → Process → Output)
- INPUT:   Sanitize & normalize raw user text
- PROCESS: Dictionary-based O(1) intent matching (not if-elif ladder!)
- OUTPUT:  Response generation with fallback
"""

# ─────────────────────────────────────────────
# KNOWLEDGE BASE — The Rule Engine
# Uses a dictionary for O(1) lookup instead of
# an if-elif ladder (which is O(n) and fragile).
# ─────────────────────────────────────────────
RESPONSES = {
    # Greetings
    "hello":        "Hello! I'm DecoBot 🤖 How can I help you today?",
    "hi":           "Hi there! Welcome to DecodeLabs. What can I do for you?",
    "hey":          "Hey! Ready to assist. What's on your mind?",
    "good morning": "Good morning! Hope you're having a great day. How can I help?",
    "good evening": "Good evening! What can I assist you with tonight?",

    # About
    "who are you":  "I'm DecoBot — a rule-based AI chatbot built at DecodeLabs. 🧠",
    "what are you": "I'm a rule-based chatbot. I match your input to predefined rules and respond instantly.",
    "what can you do": "I can answer greetings, tell you about myself, share the time, tell a joke, and more. Try asking!",

    # Utility
    "time":         f"I don't have a live clock, but Python's datetime can help: `import datetime; print(datetime.datetime.now())`",
    "help":         "Here are some things you can ask me:\n  → hello / hi / hey\n  → who are you\n  → tell me a joke\n  → what can you do\n  → bye / exit / quit",

    # Fun
    "tell me a joke":   "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "joke":             "I asked an AI to tell me a joke... it said 'I do not understand.' 😄",
    "are you smart":    "I'm deterministic — I always give the same answer for the same input. That's not smart, that's reliable! ⚙️",

    # Farewells (handled specially — they trigger exit)
    "bye":  "Goodbye! Keep building great things. 👋",
    "exit": "Goodbye! Keep building great things. 👋",
    "quit": "Goodbye! Keep building great things. 👋",
}

EXIT_COMMANDS = {"bye", "exit", "quit"}

FALLBACK = "I don't understand that yet. Type 'help' to see what I can do."


# ─────────────────────────────────────────────
# PHASE 1: INPUT & SANITIZATION
# Normalize input so "Hello", "HELLO", "  hello  "
# all map to the same key in the dictionary.
# ─────────────────────────────────────────────
def sanitize(raw_input: str) -> str:
    return raw_input.lower().strip()


# ─────────────────────────────────────────────
# PHASE 2: PROCESS — Intent Matching
# Dictionary .get() is an atomic O(1) operation:
# lookup + fallback in a single step.
# ─────────────────────────────────────────────
def get_response(clean_input: str) -> str:
    return RESPONSES.get(clean_input, FALLBACK)


# ─────────────────────────────────────────────
# PHASE 3: OUTPUT — The Continuous Loop
# The chatbot stays alive until a kill command.
# ─────────────────────────────────────────────
def run_chatbot():
    print("=" * 50)
    print("  DecoBot — Rule-Based AI Chatbot 🤖")
    print("  Type 'help' for options. Type 'exit' to quit.")
    print("=" * 50)

    while True:
        # Phase 1: Input & Sanitization
        raw_input = input("\nYou: ")
        clean_input = sanitize(raw_input)

        # Skip empty input
        if not clean_input:
            continue

        # Phase 2: Process — get the response
        response = get_response(clean_input)

        # Phase 3: Output
        print(f"Bot: {response}")

        # Exit strategy — clean break command
        if clean_input in EXIT_COMMANDS:
            break


# ─────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()
