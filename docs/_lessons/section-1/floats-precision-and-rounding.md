---
section: 1
lesson: 0
sublesson: 4
section_title: "Fundamentals of Programming"
title: "Floats - Precision and Rounding"
layout: lesson
---

# Floats (Deep Dive)

Floating-point numbers give you flexibility, but they also come with quirks. In this lesson, we’ll explore what floats can do—and where they might surprise you.

---

## Float Math Operations

All the same math operations from integers apply to floats:

```python
a = 5.5
b = 2.0

print(a + b)   # 7.5
print(a - b)   # 3.5
print(a * b)   # 11.0
print(a / b)   # 2.75
```

---

## Decimal Precision Issues

Because floats are stored in binary, some numbers can’t be represented exactly. This can lead to **small rounding errors**:

```python
print(0.1 + 0.2)  # Might print 0.30000000000000004
```

This is normal behavior in most programming languages.

---

## Rounding and Formatting

You can use Python’s `round()` function to limit how many decimal places you show:

```python
value = 1.234567
print(round(value, 2))  # 1.23
```

You can also format floats with f-strings:

```python
price = 3.456
print(f"${price:.2f}")  # $3.46
```

---

## Converting Between Types

You can convert between `int` and `float` using the `int()` and `float()` functions:

```python
x = 5
y = float(x)   # 5.0

z = 7.9
w = int(z)     # 7 (truncates, doesn't round)
```

---

## Summary

- Floats are great for precision but can introduce tiny rounding errors.
- Use `round()` or string formatting when working with money or UI.
- Converting between types is easy, but be aware that `int()` drops the decimal part.

> 💡 Deep dive complete! You now know how to work with floats in a variety of real-world scenarios.
