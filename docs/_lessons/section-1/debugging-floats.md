---
section: 1
lesson: 0
sublesson: 6
section_title: "Fundamentals of Programming"
title: "Debug Zone - Floats"
layout: lesson
---

## 🐞 Debug Zone - Floats and Unexpected Errors

In the real world, floating-point numbers are everywhere-prices, averages, measurements-and so are the bugs they can cause.

In this section, we'll look at a practical example involving budgeting and walk through a real Python error using something called a **stack trace**.

---

### 💸 Calculating an Average - Practical Example

Let's say you're trying to average your grocery spending over a few weeks:

```python
expenses = [52.35, 48.90, 61.42, 0]
weeks = len(expenses)

average = sum(expenses) / weeks
print("Average weekly cost: $" + average)
```

#### ❌ What Went Wrong?

Here's the error you'll get if you run this code:

```plaintext
Traceback (most recent call last):
  File "budget.py", line 5, in <module>
    print("Average weekly cost: $" + average)
TypeError: can only concatenate str (not "float") to str
```

Let's break that down:

---

### 🔍 Understanding the Stack Trace

#### ➤ `Traceback (most recent call last):`  
This tells you an error occurred and Python is going to show you *where* it happened.

#### ➤ `File "budget.py", line 5, in <module>`  
You're looking at line 5 of your file, which is where the problem occurred. That's this line:

```python
print("Average weekly cost: $" + average)
```

#### ➤ `TypeError: can only concatenate str (not "float") to str`  
This is the *actual* error: Python is telling you it can't combine a `str` (the dollar sign part) with a `float` (your average number). That's what the `+` operator was trying to do.

---

### ✅ Fix It by Casting the Float

```python
print("Average weekly cost: $" + str(average))
```

Or, even better formatting:

```python
print(f"Average weekly cost: ${average:.2f}")
```

---

### 🧠 Debugging Tip - Read the Whole Error

Beginners often panic when they see a long error message. But stack traces are like breadcrumbs. Start at the bottom and read upward:
- What type of error?
- What line caused it?
- What does Python *say* about the problem?

The answer is usually right there-you just need to slow down and read it.

---

### 🚫 Bad Debugging Habit - Blaming the Wrong Line

Sometimes the real issue starts before the line where the crash happens. For example, if `weeks` had been 0, this line:

```python
average = sum(expenses) / weeks
```

Would've crashed with a `ZeroDivisionError`.

That's why it's helpful to check your input first and use `print()` to double-check assumptions while you debug.

---

### 🧠 Rubber Duck Reminder

Still stuck? Try explaining your code to someone-or something. Talk through your logic step-by-step, even if it's just to a rubber duck on your desk.

---

This section introduced stack traces and the importance of reading error messages carefully. In future lessons, we'll practice even more techniques to help you build confident, bug-free code.
