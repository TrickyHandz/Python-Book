---
section: 0
lesson: 2
sublesson: 0
section_title: "Getting Started"
title: "Interpreted vs Compiled Languages"
layout: lesson
---

# Interpreted vs Compiled Languages

Before we start writing Python code, it helps to understand **how programming languages work** under the hood—especially the difference between **interpreted** and **compiled** languages. This will give you a clearer picture of what Python is doing behind the scenes.

## What is a Compiled Language?

Compiled languages—like **C**, **C++**, or **Rust**—require the entire program to be converted into machine code (binary) before it can run. This is done by a special program called a **compiler**.

- ✅ Runs very fast once compiled.
- 🛠 Must compile every time you make a change.
- 📦 Produces standalone executable files.

### Example:
When you compile a C program, it becomes a `.exe` or `.out` file that can run without the original source code.

## What is an Interpreted Language?

Interpreted languages—like **Python**, **JavaScript**, or **Ruby**—do not require compiling in advance. Instead, they run line-by-line using an **interpreter** that reads and executes the code on the fly.

- ⚡ Easier to test quickly.
- 🔄 Slower at runtime compared to compiled languages.
- 🧪 Great for learning, scripting, and rapid development.

### Example:
When you run a Python file, the Python interpreter reads each line and executes it immediately.

## Where Python Falls

Python is considered an **interpreted language**. You write code in a `.py` file, and Python executes it line by line using the Python interpreter.

This makes it:
- Great for scripting and small tasks.
- Friendly to beginners—easy to read, write, and test.
- Slightly slower than compiled languages for very large or performance-critical programs.

## Why This Matters

Understanding this difference helps you choose the right tool for the job:
- Want to build low-level, high-performance software? Go compiled.
- Want to write readable, flexible scripts or automate things quickly? Go interpreted.

> 🧠 **Takeaway**: Python is interpreted, meaning it's fast to write and test, and perfect for learning—even if it sacrifices some speed compared to compiled languages.

