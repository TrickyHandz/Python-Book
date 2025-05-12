---
section: 1
lesson: 0
sublesson: 7
section_title: "Python Fundamentals"
title: "Strings"
layout: lesson
---

# Strings

### What Is a String?

In Python, a **string** is a sequence of characters used to represent text. Strings can contain letters, numbers, symbols, and even spaces. They are one of the most commonly used data types in any programming language.

---

### How Do You Make a String?

Strings are created by placing text between quotes. Python allows you to use either **single quotes** (`'`) or **double quotes** (`"`), and both work the same way.

Examples:
- `'hello'`
- `"this is a string"`
- `'1234'`

---

### Why Are Strings Important?

Strings are used to:
- Display messages to users
- Store names, file paths, URLs, and other textual data
- Process and analyze text from files or input
- Communicate with the outside world (APIs, logs, UI, etc.)

Whether you're printing text to the screen, receiving user input, or logging error messages, you're probably working with strings.

---

### What Can Strings Contain?

A string can hold:
- A single character (`'a'`)
- A word (`"hello"`)
- A sentence (`'This is a complete sentence.'`)
- Even an empty value (`""`) — this is called an **empty string**

---

### A Note About Quotes

If you use single quotes to create a string, you can still use double quotes *inside* the string, and vice versa. This is helpful when working with quotes in text.

Examples:
- `'She said, "Hello."'`
- `"It's a good day."`

For more complex cases, Python also supports **triple quotes** (`'''` or `"""`) for multiline strings, which we'll cover later.

---

### Strings Are Immutable

Once a string is created, its content cannot be changed. This is called **immutability**. If you want to "change" a string, you must create a new one instead. This helps prevent accidental data corruption and improves reliability in larger programs.

