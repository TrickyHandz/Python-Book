---
section: 1
lesson: 0
sublesson: 3
section_title: "Fundamentals of Programming"
title: "Floats"
layout: lesson
---

# Floats

A **float** (short for "floating point number") is a number with a decimal point. Floats are used whenever you need more precision than whole numbers can provide—like when working with measurements, averages, or money.

---

## Declaring Float Variables

You can create a float by using a decimal:

```python
pi = 3.14
temperature = -10.5
```

Even whole-looking numbers like `5.0` are considered floats:

```python
price = 5.0
```

---

## Type Checking

```python
print(type(pi))  # <class 'float'>
```

This confirms you're working with a float instead of an integer.

---

## Division Returns Floats

In Python, using the `/` operator always returns a float:

```python
result = 10 / 2
print(result)  # 5.0
```

Even if the result is a whole number, the type will be `float`.

---

## Summary

- Floats are numbers with decimals.
- Python treats numbers with a `.` as floats automatically.
- Division using `/` returns floats, even when the result is whole.

