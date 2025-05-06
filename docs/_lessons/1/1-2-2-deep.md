---
layout: default
title: "Lesson 1.2.1 – Floats – Deep Dive"
section: 1
lesson: 2
sublesson: 2.1
order: 8
---

# 1.2.2 Deep Dive – Floating Point Numbers in Python

Floating point numbers (floats) in Python represent real numbers, including fractions. They follow the IEEE 754 standard for binary floating-point arithmetic, which means they sometimes behave in unexpected ways due to rounding errors.

For example:

```python
print(0.1 + 0.2)  # 0.30000000000000004
```

This behavior is normal in most languages that follow the standard and is something to be aware of when working with precise values like currency. Use the `decimal` module when exact decimal representation is needed.
