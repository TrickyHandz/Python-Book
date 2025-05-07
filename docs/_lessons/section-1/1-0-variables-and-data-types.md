---
section: 1
lesson: 0
sublesson: 0
section_title: "Fundamentals of Programming"
title: "Variables and Data Types"
layout: lesson
---

# Variables and Data Types

Now that your Python environment is ready, it’s time to start writing code. One of the first things every programmer needs to understand is how to **store data** and **work with different types of information**. In Python, this starts with **variables** and **data types**.

---

## What Is a Variable?

A **variable** is a name you assign to a value in memory. Think of it like a labeled box: you put something inside the box and label it so you can refer to it later.

```python
name = "Alice"
age = 30
```

In the example above:
- `name` is a variable that stores the string `"Alice"`
- `age` is a variable that stores the number `30`

---

## Common Data Types in Python

Python has several **built-in data types**. Here are some of the most common:

| Type     | Example        | Description                     |
|----------|----------------|---------------------------------|
| `int`    | `42`           | Integer (whole number)          |
| `float`  | `3.14`         | Decimal number                  |
| `str`    | `"hello"`      | String (text)                   |
| `bool`   | `True`, `False`| Boolean (true or false)         |

You can check the type of a value with the `type()` function:

```python
print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>
```

---

## Naming Variables

Python has a few rules and best practices for naming variables:

✅ Allowed:
- Letters (a–z, A–Z)
- Numbers (0–9), but **not** at the beginning
- Underscores (`_`)

❌ Not Allowed:
- Spaces or special characters
- Reserved words like `print`, `if`, or `while`

Recommended style:
```python
user_name = "bob"
is_active = True
```

---

## Reassigning Variables

Variables can change during a program:

```python
score = 100
score = score + 10  # Now score is 110
```

Python will always remember the most recent value you gave a variable.

---

## Quick Recap

- Variables store data you can use later.
- Python is dynamically typed—you don’t have to declare the data type.
- Common data types include integers, floats, strings, and booleans.

> 💡 You’ll use variables constantly in Python, so get comfortable naming them clearly and keeping track of what they hold.

---

Ready to practice? Try writing a few variables of your own in the REPL or your editor!

