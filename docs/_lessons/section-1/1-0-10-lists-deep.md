---
section: 1
lesson: 0
sublesson: 10
section_title: "Fundamentals of Programming"
title: "Lists (Deep Dive)"
layout: lesson
---

# Lists (Deep Dive)

Now that you know how to create and use lists, let’s explore some powerful list features and methods.

---

## List Slicing

You can get a portion of a list with slicing:

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # [20, 30, 40]
print(numbers[:3])   # [10, 20, 30]
```

---

## Common List Methods

| Method        | Description                                |
|---------------|--------------------------------------------|
| `.append(x)`  | Adds an item to the end                    |
| `.insert(i,x)`| Inserts at a specific index                |
| `.remove(x)`  | Removes the first occurrence of x          |
| `.pop()`      | Removes and returns the last item          |
| `.sort()`     | Sorts the list in-place                    |
| `.reverse()`  | Reverses the order in-place                |

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']
```

---

## Looping Through a List

You can iterate over lists using a `for` loop:

```python
colors = ["red", "green", "blue"]
for color in colors:
    print(color)
```

---

## Nesting and Complex Lists

Lists can contain other lists:

```python
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(matrix[1][0])  # 3
```

---

## Summary

- Lists support slicing, sorting, and iteration.
- Use built-in methods to manipulate list contents.
- Lists can hold anything—including other lists.

> 💡 Mastering lists is essential for handling collections of data in Python.
