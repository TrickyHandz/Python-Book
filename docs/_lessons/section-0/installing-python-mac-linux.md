---
section: 0
lesson: 5
sublesson: 0
section_title: "Getting Started"
title: "Installing Python on Mac and Linux"
layout: lesson
---

# Installing Python on Mac and Linux

Python comes pre-installed on many Mac and Linux systems—but not always in the version you need. Here’s how to make sure you have the latest version installed and ready to use.

---

## 🐍 macOS Installation

### Option 1: Use the Official Installer

1. Visit [https://www.python.org/downloads/mac-osx/](https://www.python.org/downloads/mac-osx/)
2. Download the latest version for macOS (`.pkg` file).
3. Open the downloaded file and follow the installation steps.

### Option 2: Use Homebrew (Recommended for Developers)

If you already have [Homebrew](https://brew.sh/) installed:

```bash
brew install python
```

After installation, verify it:

```bash
python3 --version
```

> 💡 Note: On macOS, you often need to use `python3` instead of `python` in the terminal.

---

## 🐧 Linux Installation

### Debian/Ubuntu-based Systems

Use `apt` to install Python:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Fedora-based Systems

Use `dnf`:

```bash
sudo dnf install python3 python3-pip
```

### Arch-based Systems

Use `pacman`:

```bash
sudo pacman -S python python-pip
```

After installation, test it with:

```bash
python3 --version
```

---

## Verify pip (Python Package Installer)

Make sure `pip` is also available:

```bash
pip3 --version
```

If `pip` isn’t installed, you can usually add it with:

```bash
sudo apt install python3-pip  # Debian/Ubuntu
```

---

## Which Version Should I Use?

You should be using **Python 3.10 or later**. Avoid Python 2 unless you’re working with legacy software.

> 🧠 **Tip**: Don’t worry if your system has multiple Python versions. You can explicitly use `python3` and `pip3` to make sure you’re using the right one.

---

Once installed, you’re ready to write and run Python code on your system using a terminal or code editor.
