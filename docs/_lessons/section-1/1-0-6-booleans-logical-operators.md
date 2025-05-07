---
section: 1
lesson: 0
sublesson: 6
section_title: "Fundamentals of Programming"
title: "Booleans - Logical Operators"
layout: lesson
---

# Booleans (Deep Dive)

Let’s go deeper into how booleans work in Python—including how other values can be treated as true or false.

---

## Boolean Operators

Booleans support logic operations:

| Operator | Description      | Example           | Result |
|----------|------------------|-------------------|--------|
| `and`    | Both must be true| `True and False`  | False  |
| `or`     | One must be true | `True or False`   | True   |
| `not`    | Inverts value    | `not True`        | False  |

```python
logged_in = True
is_admin = False

print(logged_in and is_admin)  # False
print(logged_in or is_admin)   # True
```

---

## Truthy and Falsy Values

In Python, some values **automatically evaluate to `False`** in a boolean context:

```python
False
None
0
0.0
""
[]
{}
set()
```

Everything else is considered **truthy** (evaluates to `True`).

```python
if []:
    print("This won't run")
if [1, 2, 3]:
    print("This will run")
```

---

## Using Booleans in Control Flow

```python
age = 20
if age >= 18:
    print("You can vote!")
else:
    print("Not old enough.")
```

---

## Summary

- Booleans control logic in your programs.
- Use `and`, `or`, and `not` to build complex expressions.
- Empty values like `0`, `""`, or `[]` are falsy—everything else is truthy.

> 💡 Mastering booleans helps you write smarter conditions and cleaner control structures.

