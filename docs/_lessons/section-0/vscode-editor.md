---
section: 0
lesson: 8
sublesson: 0
section_title: "Getting Started"
title: "Using Visual Studio Code"
layout: lesson
---

# Using Visual Studio Code

**Visual Studio Code (VS Code)** is a powerful, customizable code editor that works across platforms and supports Python extremely well. If you're planning to write more complex programs or want a professional-grade tool, VS Code is an excellent choice.

---

## Step 1: Install Visual Studio Code

1. Go to [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Download the version for your operating system.
3. Run the installer and follow the setup steps.

> 💡 **Tip**: On Windows, allow the installer to add VS Code to your system PATH and register it as a right-click menu option.

---

## Step 2: Install the Python Extension

1. Open VS Code.
2. Go to the **Extensions** tab (or press `Ctrl+Shift+X`).
3. Search for **Python** and install the extension by Microsoft.

This extension provides:
- Code linting (error highlighting)
- IntelliSense (autocomplete)
- Code formatting
- Integrated terminal support
- Debugging tools

---

## Step 3: Select Your Python Interpreter

After installing the Python extension, press `Ctrl+Shift+P` to open the **Command Palette**, then:

```
Python: Select Interpreter
```

Choose the version of Python you installed earlier (it should show the path and version).

---

## Step 4: Open or Create a Python File

1. Click `File → New File` or open an existing `.py` file.
2. Save it with a `.py` extension if it’s new.
3. Start coding!

To run the script:
- Use the green **Run** button at the top right
- Or use `Ctrl+F5` to run without debugging

---

## Step 5: Use the Integrated Terminal

VS Code comes with a built-in terminal:

- Open it with `` Ctrl+` `` or go to `View → Terminal`
- This lets you run Python scripts using:

```bash
python your_script.py
```

---

## Why Use VS Code?

- 🧠 Autocompletion and real-time feedback
- 🐞 Built-in debugger
- 🔌 Supports thousands of extensions
- 🪄 Great for scripting, web dev, data science, and more

---

## Things to Watch Out For

- VS Code may not detect your Python install unless it’s properly added to PATH (especially on Windows).
- Some features require you to install additional tools like `pylint` or `black`.

---

## Summary

VS Code is the recommended environment for this course if you're ready to move beyond the basics. It's fast, modern, and gives you all the tools you need to grow as a Python developer.

> 🚀 **Pro Tip**: You don’t need to master VS Code to get started—just install the Python extension and start writing code. The more you use it, the more powerful it becomes.

