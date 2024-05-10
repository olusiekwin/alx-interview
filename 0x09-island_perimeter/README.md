# 0x09. Island Perimeter

## 0x09. Island Perimeter

**Project Description**

This project focuses on calculating the perimeter of a single island within a grid represented by a 2D array of integers in Python. It assesses your understanding of algorithms, data structures (2D lists), and conditional logic to solve a geometric problem.

**Concepts Covered**

* **2D Arrays (Matrices):** Accessing, iterating, navigating horizontally/vertically through elements, and understanding adjacent cells.
* **Conditional Logic:** Applying conditions to identify cells contributing to the perimeter.
* **Counting Techniques:** Developing a method to count perimeter edges.
* **Problem-Solving Strategies:** Breaking down the problem to identify land cells and calculate their perimeter contribution.
* **Python Programming:** Nested loops for iterating over grid cells, conditional statements for checking adjacent cells.

**Resources**

* **Python Official Documentation:** Nested Lists
* **GeeksforGeeks Articles:** Python Multi-dimensional Arrays
* **TutorialsPoint:** Python Lists ([https://www.tutorialspoint.com/python_data_structure/python_lists_data_structure.htm](https://www.tutorialspoint.com/python_data_structure/python_lists_data_structure.htm))
* **YouTube Tutorials:** Python 2D arrays and lists

**Requirements**

* **Editors:** vi, vim, emacs
* **Python Version:** 3.4.3 on Ubuntu 20.04 LTS
* **Line Endings:** All files must end with a new line
* **First Line:** The first line of all files should be `#!/usr/bin/python3`
* **README.md:** Mandatory file at the project root
* **Code Style:** PEP 8 (version 1.7)
* **Module Imports:** None allowed (code must be self-contained)
* **Documentation:** All modules and functions must be documented
* **Executable Files:** All files must be executable

**Task**

**0. Island Perimeter (Mandatory)**

Create a function `def island_perimeter(grid)` that returns the perimeter of the island described in `grid`:

* `grid` is a list of lists of integers:
    * 0 represents water
    * 1 represents land
* Each cell is a square with a side length of 1.
* Cells are connected horizontally/vertically (not diagonally).
* `grid` is rectangular (width and height not exceeding 100).
* The grid is completely surrounded by water.
* There is only one island (or nothing).
* The island doesn't have "lakes" (water inside not connected to the surrounding water).

**Example**

```
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

perimeter = island_perimeter(grid)
print(perimeter)  # Output: 12
```

**Repo**

* **GitHub Repository:** alx-interview
* **Directory:** 0x09-island_perimeter

**Grading**

* The provided code will be auto-reviewed upon the deadline.

**Additional Notes**

This project strengthens your algorithmic thinking, data structure manipulation skills, and logical reasoning to solve problems. 

**Start coding and good luck!**

