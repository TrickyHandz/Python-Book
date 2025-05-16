---
section: 0
lesson: 4
sublesson: 0
section_title: "Getting Started"
title: "Installing Python on Windows"
layout: lesson
---

# Installing Python on Windows

To run Python on your own computer, you’ll need to install it first. This guide will walk you through installing Python on a Windows system in a way that works well with tools like **VS Code** and **PowerShell**.

## Step 1: Download the Python Installer

1. Visit the official Python download page:  
   [https://www.python.org/downloads/windows](https://www.python.org/downloads/windows)
2. Click the button for the latest stable version (e.g., “Python 3.x.x”).

## Step 2: Run the Installer

1. Launch the downloaded `.exe` file.
2. **Important**: Check the box that says **"Add Python to PATH"** before doing anything else.
3. Choose **"Install Now"** for a simple setup.

This will install:
- The Python interpreter
- `pip`, the Python package manager
- `IDLE`, the basic editor
- Documentation and standard libraries

## Step 3: Confirm the Installation

1. Open the **Start Menu** and type `cmd`, then open the **Command Prompt**.
2. Type:

   ```bash
   python --version
   ```

   You should see something like:

   ```
   Python 3.x.x
   ```

3. You can also try:

   ```bash
   python
   ```

   to open the interactive Python prompt. Exit it with `exit()` or `Ctrl+Z`, then `Enter`.

## Alternative: Use the Microsoft Store Version

Some tools (like **VS Code**) work more smoothly if Python was installed from the **Microsoft Store**.

To install this version:
1. Open the **Microsoft Store** on your Windows machine.
2. Search for "Python".
3. Install the latest version by the Python Software Foundation.

You may need to restart your terminal for it to be recognized.

> 🧠 **Tip**: If you install from the official website, always ensure "Add Python to PATH" is checked. If you install from the Store, Python will be available globally—but you may need to install `pip` separately for some environments.

## What’s Next?

Once Python is installed, you'll be able to run `.py` files, install packages, and work with code in VS Code, IDLE, or the terminal. In the next lessons, we’ll explore each of these tools.

