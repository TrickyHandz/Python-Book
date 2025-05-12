---
section: 1
lesson: 0
sublesson: 8
section_title: "Python Fundamentals"
title: "Strings - Concatenation and Methods"
layout: lesson
---

## Strings – Concatenation and Methods

Now that you’ve seen what a string is, let’s look at how you can work with them using some common operations and built-in methods.

---

### 🔗 String Concatenation

**Concatenation** means joining two or more strings together into one.

You can use the `+` operator to combine strings:

```python
first = "Hello"
second = "world"
combined = first + " " + second
print(combined)  # Output: Hello world
```

You can also build longer strings by chaining multiple concatenations:

```python
greeting = "Good" + " " + "morning" + ", " + "everyone!"
```

---

### 🔁 Repeating Strings

You can repeat a string using the `*` operator:

```python
laugh = "ha" * 3
print(laugh)  # Output: hahaha
```

---

### 🔍 Useful String Methods

Python strings come with built-in methods that allow you to transform and inspect them easily.

#### `.upper()`  
Converts all characters to uppercase.

```python
name = "alice"
print(name.upper())  # Output: ALICE
```

#### `.lower()`  
Converts all characters to lowercase.

```python
greeting = "HELLO"
print(greeting.lower())  # Output: hello
```

#### `.capitalize()`  
Makes only the first character uppercase.

```python
text = "python"
print(text.capitalize())  # Output: Python
```

#### `.replace(old, new)`  
Replaces parts of a string.

```python
phrase = "I like cats"
print(phrase.replace("cats", "dogs"))  # Output: I like dogs
```

#### `.startswith()` and `.endswith()`  
Check if a string begins or ends with a certain value.

```python
filename = "report.pdf"
print(filename.startswith("report"))  # True
print(filename.endswith(".docx"))     # False
```

---

### 🔍 Finding String Length

Use `len()` to find out how many characters are in a string:

```python
message = "hello"
print(len(message))  # Output: 5
```

---

### 🧠 Summary

- Use `+` to join strings.
- Use `*` to repeat a string.
- Built-in methods like `.upper()`, `.lower()`, `.replace()` help you work with string data.
- `len()` tells you how many characters are in a string.
