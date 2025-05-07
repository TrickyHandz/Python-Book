---
section: 1
lesson: 0
sublesson: 1
section_title: "Fundamentals of Programming"
title: "Integers: Basic Usage"
layout: lesson
---

# Integers: Basic Usage

An **integer** (or `int`) is a whole number—meaning it has no decimal point. Integers are one of the most common data types in programming, and Python makes it easy to work with them.

---

## Declaring Integer Variables

You don't need to specify the type—just assign a whole number:

```python
count = 10
year = 2025
```

You can print them or use them in expressions:

```python
print(count)
print("Next year will be", year + 1)
```

---

## Negative and Large Integers

Python supports:
- Negative integers: `-1`, `-100`
- Large integers: `1000000000000` (no size limit other than memory)

```python
balance = -500
big_number = 9999999999999999
```

---

## Type Checking

```python
print(type(count))  # <class 'int'>
```

This confirms you're working with an integer.

---

## Summary

- Integers are whole numbers.
- You can assign and use them directly.
- Python handles big and small integers without extra syntax.

