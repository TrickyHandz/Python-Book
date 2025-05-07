---
section: 0
lesson: 6
sublesson: 0
section_title: "Getting Started"
title: "Using the Interactive Terminal (REPL)"
layout: lesson
---

# Using the Interactive Terminal (REPL)

Once you’ve installed Python, the simplest way to start experimenting with code is through the **interactive terminal**, also known as the **REPL** (Read–Eval–Print Loop).

This is a great place to test small bits of code, try out syntax, or understand how something works—without having to write a full script.

---

## Starting the Python REPL

### On Windows (Command Prompt or PowerShell)

```bash
python
```

If that doesn't work, try:

```bash
python3
```

### On macOS or Linux (Terminal)

```bash
python3
```

---

## What It Looks Like

You’ll see a prompt like this:

```
>>>
```

Now you can type Python commands one line at a time:

```python
>>> print("Hello, world!")
Hello, world!
```

---

## Why Use the REPL?

- 🧪 Quickly test ideas
- 🧵 Check the value of expressions
- 🔎 Explore built-in functions
- 🧰 Great for debugging and experimenting

You can also use the REPL to import modules and run simple calculations:

```python
>>> import math
>>> math.sqrt(16)
4.0
```

---

## Exiting the REPL

To exit:
- Type `exit()` and press Enter
- OR press `Ctrl+Z` then Enter (on Windows)
- OR press `Ctrl+D` (on macOS/Linux)

---

## Advanced Tip: Use IPython or bpython

Once you're more comfortable, tools like **IPython** or **bpython** offer richer interactive experiences with history, autocomplete, and syntax highlighting.

But for now, the built-in REPL is perfect.

> 💡 **Tip**: When learning, open a terminal and keep the REPL running in the background. It’s a fast way to test new ideas as you read through lessons.

