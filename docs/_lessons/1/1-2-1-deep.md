---
layout: default
title: "Integers – Deep Dive"
section: 1
lesson: 2
sublesson: 1
order: 4
---

# 1.2.1 Deep Dive – Integers in Python

Python makes working with numbers simple, but there's more going on beneath the surface when it comes to integers. Python supports arbitrarily large integers out of the box, so you don’t have to worry about integer overflow like in many other languages.

This flexibility allows you to work with very large numbers:

```python
big_number = 9876543210123456789
print(big_number * 2)
```

Python integers also interact well with other numeric types, automatically promoting results to `float` or other types when needed.
