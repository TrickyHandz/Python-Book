---
layout: default
title: "Booleans – Deep Dive"
section: 1
lesson: 2
sublesson: 3.1
order: 7
---

# 1.2.3 Deep Dive – Boolean Values in Python

Booleans in Python represent truth values: `True` and `False`. These are the building blocks of conditional logic, allowing you to control the flow of your programs.

## Truthiness and Falsiness

Not all values in Python are explicitly `True` or `False`, but they can still behave as such. Python determines the "truthiness" or "falsiness" of values in conditions.

**Falsy values include:**
- `False`
- `None`
- `0` (any numeric type)
- `""` (empty string)
- `[]`, `{}`, `()`, `set()` (empty collections)

Everything else is considered **truthy**.

```python
if "hello":
    print("This is truthy!")

if []:
    print("This won’t print.")
```
