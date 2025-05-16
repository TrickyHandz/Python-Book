---
section: 1
lesson: 0
sublesson: 10
section_title: "Python Fundamentals"
title: "Lists – Indexing and Manipulation"
layout: lesson
---

## Lists – Indexing and Manipulation

Now that you know how to create and use lists, let’s explore how to work with individual elements, manipulate list contents, and take advantage of Python’s powerful built-in methods.

---

### 🔢 Indexing and Selection

Lists are **ordered collections**. That means every item has a **position**, or **index**.

Indexing starts at **0**, so the first item in a list is at position `0`, the second is at `1`, and so on.

```python
colors = ["red", "green", "blue"]
print(colors[0])  # red
print(colors[2])  # blue
```

This is how you **select** a single element from a list: by its index.

Negative indexes count from the end:

```python
print(colors[-1])  # blue
print(colors[-2])  # green
```

---

### 🪒 List Slicing

Sometimes you want a **part of a list**, not just one item. This is called **slicing**.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])  # [20, 30, 40] – from index 1 to 3 (4 is not included)
print(numbers[:3])   # [10, 20, 30] – from the beginning up to index 3
print(numbers[2:])   # [30, 40, 50] – from index 2 to the end
```

Slicing is a form of **selection** — it lets you extract a **range** of items from a list.

---

### 🧰 Common List Methods

Here are some powerful tools you can use to manipulate lists:

| Method        | Description                         |
|--------------|-------------------------------------|
| `.append(x)` | Adds an item to the end             |
| `.insert(i,x)` | Inserts `x` at index `i`         |
| `.remove(x)` | Removes the first occurrence of `x` |
| `.pop()`     | Removes and returns the last item   |
| `.sort()`    | Sorts the list in place             |
| `.reverse()` | Reverses the list in place          |

Example:

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

fruits.remove("banana")
print(fruits)  # ['apple', 'cherry']
```

---

### 🔁 Looping Through a List

You can use a `for` loop to process each item in a list:

```python
colors = ["red", "green", "blue"]

for color in colors:
    print(color)
```

This lets you perform the same action on each element — useful for filtering, formatting, or processing data.

> 📝 **Note:** If you're not sure how `for` loops work yet, don’t worry! We'll cover loops in detail later. For now, just know that you can use a loop to go through each item in a list one at a time.

---

### 🧱 Nesting and Complex Lists

Lists can contain **other lists**, which allows you to store structured or tabular data:

```python
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print(matrix[1][0])  # Output: 3
```

Here, `matrix[1]` selects the second row `[3, 4]`, and `[1][0]` grabs the first element of that row.

---

### 🧠 Summary

- Lists use **indexing** to select individual items.
- **Slicing** is a form of selection that lets you extract sublists.
- Use methods like `.append()`, `.remove()`, and `.sort()` to manipulate list contents.
- You can loop through a list to process elements one by one.
- Lists can hold any type of data — even other lists.

💡 Mastering list manipulation is essential for handling collections of data in Python.
