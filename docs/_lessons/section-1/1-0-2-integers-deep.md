---
section: 1
lesson: 0
sublesson: 2
section_title: "Fundamentals of Programming"
title: "Integers: Math and Operations"
layout: lesson
---

# Integers: Math and Operations

Now that you know how to store integers, let’s look at what you can do with them.

Python supports basic math operations right out of the box.

---

## Arithmetic Operators

| Operation      | Symbol | Example        | Result |
|----------------|--------|----------------|--------|
| Addition       | `+`    | `2 + 3`        | `5`    |
| Subtraction    | `-`    | `5 - 1`        | `4`    |
| Multiplication | `*`    | `4 * 2`        | `8`    |
| Division       | `/`    | `10 / 2`       | `5.0`  |
| Floor Division | `//`   | `7 // 2`       | `3`    |
| Modulus        | `%`    | `7 % 2`        | `1`    |
| Exponentiation | `**`   | `2 ** 3`       | `8`    |

> 🔍 Division with `/` always returns a float—even if the result is whole.

---

## Combining Operations

Python respects **order of operations (PEMDAS)**:

```python
result = 2 + 3 * 4  # 14
```

Use parentheses to change the order:

```python
result = (2 + 3) * 4  # 20
```

---

## Updating Values

You can use `+=`, `-=`, `*=`, etc., to update variables:

```python
score = 10
score += 5  # Now 15
score *= 2  # Now 30
```

---

## Summary

- Python handles math operations using symbols you're already familiar with.
- Be aware of integer vs float results.
- Compound assignment operators (`+=`, `-=`, etc.) make updating values easy.

> 💡 Practice by writing a small calculator script or experimenting in the REPL.

