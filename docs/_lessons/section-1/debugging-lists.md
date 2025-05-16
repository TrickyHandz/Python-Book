---
section: 1
lesson: 0
sublesson: 13
section_title: "Fundamentals of Programming"
title: "Debug Zone – Lists"
layout: lesson
---

## 🐞 Debug Zone – Lists and Common Pitfalls

Lists are a powerful tool for storing and organizing data—but they also come with their own set of common bugs. In this Debug Zone, we’ll walk through a few realistic errors using a simple **task list**, and we’ll show both **bad debugging habits** and **better solutions**.

---

### 📋 Setup – A Simple Task List

    tasks = ["buy groceries", "clean kitchen", "walk dog"]

---

### ❌ Bug #1 – IndexError

    print("Task 4:", tasks[3])

#### Output:

    IndexError: list index out of range

#### What Happened?  
You asked for the 4th item, but lists in Python start at 0. The index `3` is out of bounds for a 3-item list.

#### Bad Debugging Move:  
> “I just changed the index to 0 and it worked.”

**Why it’s a problem:** You fixed the crash, but not the real issue—now you're printing the wrong task.

#### Better Fix:

    if len(tasks) > 3:
        print("Task 4:", tasks[3])
    else:
        print("Not enough tasks to show Task 4.")

---

### ❌ Bug #2 – TypeError from Misuse of append()

    tasks = tasks.append("do laundry")
    print("Tasks:", tasks)

#### Output:

    Tasks: None

#### What Happened?  
`.append()` modifies the list in place and returns `None`. Assigning it back to `tasks` overwrites your list!

#### Bad Debugging Move:  
> “I changed it to use `+` with a string and that fixed it.”

**Why it’s a problem:** That creates a new list but might break later when you try to loop through mixed types.

#### Better Fix:

    tasks.append("do laundry")
    print("Tasks:", tasks)

---

### ✅ Debugging Tips for Lists

- Use `len()` to guard against index errors
- Print your list *before and after* changes to track what’s happening
- Don’t overwrite a list by mistake—understand what list methods return
- Think before you fix: understand the *why*, not just the *what*

---

Each of these examples shows a bug, a poor way to handle it, and a better practice. The more you practice reading errors and correcting behavior thoughtfully, the easier it becomes.

In future sections, we’ll come back to this task list idea and build something even more powerful.
