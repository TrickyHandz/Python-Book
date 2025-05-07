---
section: 1
lesson: 0
sublesson: 9
section_title: "Fundamentals of Programming"
title: "Lists"
layout: lesson
---

# Lists

**Lists** are one of the most commonly used data types in Python. A list lets you store a collection of items—like numbers, strings, or even other lists—in a single variable.

---

## Creating a List

Use square brackets to create a list:

```python
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
```

Lists can hold any data type—even mixed types:

```python
mixed = [42, "hello", True]
```

---

## Accessing Items

Use indexing (starting at 0) to access list elements:

```python
print(numbers[0])  # 1
print(names[1])    # Bob
```

You can also use negative indexes:

```python
print(names[-1])  # Charlie (last item)
```

---

## Modifying Items

Lists are **mutable**, meaning you can change them:

```python
names[0] = "Ann"
print(names)  # ['Ann', 'Bob', 'Charlie']
```

---

## Summary

- Lists store ordered groups of data.
- Access items with `[]` and index numbers.
- Lists are mutable—you can change them after creation.
