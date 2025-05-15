## 🐞 Debug Zone – Getting Started with Debugging

When you're working with numbers in Python, it’s easy to run into small mistakes—like trying to divide by zero or forgetting how integer division works. That’s where **debugging** comes in: it’s the process of finding and fixing problems in your code.

In this lesson’s Debug Zone, we’ll introduce a few beginner-friendly strategies and show you how to avoid common pitfalls when working with integers.

### 🧠 Desk Checking: Think Before You Run

One of the most powerful ways to debug is something called **desk checking**. This means going through your code one step at a time *before* you run it, and writing down what you expect to happen. 

Try reading your code like you're the computer:
- What happens first?
- What values are stored?
- What gets printed or calculated?

Even if you’re just jotting it down on scratch paper, desk checking helps you spot mistakes before they turn into errors.

### 🧱 Common Integer Errors

Here’s a buggy example. Can you spot the issue?

```python
score = 10
bonus = 2
total = score / bonus - 2
print("Final score is " + total)
```

This code will crash with a `TypeError` because `total` is a number, and Python doesn’t let you combine numbers and strings using `+` like that.

**Fix:**  
Convert the number to a string before printing:
```python
print("Final score is " + str(total))
```

### 🦆 Rubber Ducky Debugging

Sometimes the best way to find a bug is to explain your code to someone else—even if that someone is a rubber duck. Seriously.

**Rubber duck debugging** is when you talk through your code out loud, step-by-step. Explaining forces you to slow down and often reveals what’s going wrong. Try it next time you’re stuck.

### ⚠️ Bad Debugging Habits to Avoid

Let’s be honest: we all do this at first.

- **Shotgun debugging:** Changing random bits of code to see if something works. It’s usually confusing and makes things worse.
- **Print spam:** Leaving a bunch of `print()` statements in your code long after you’ve fixed the bug. It clutters things up and can hide real problems.

As you get better at debugging, you’ll start building cleaner habits—and we’ll keep practicing them as we go.
