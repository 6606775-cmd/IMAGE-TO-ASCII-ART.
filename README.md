# IMAGE-TO-ASCII-ART.
#  Image to ASCII Art using Python

## 1. Project Purpose
The purpose of this project is to demonstrate how an image can be represented in **ASCII format** using **pure Python logic**.

Instead of using any image processing libraries, the program manually constructs an ASCII image by mapping **row and column positions** to specific characters using **loops and conditional statements**.

This project focuses on:
- Understanding nested loops  
- Practicing `if / elif` conditions  
- Learning pattern-based logic  
- Console-based visual output  

---

## 2.How the Code Works
- The image is treated as a **2D grid** of fixed size (`height × width`).
- Two nested `for` loops iterate through each **row** and **column`.
- For each `(row, column)` position, a character is selected using `if` and `elif` conditions.
- Different ASCII characters (`. : - = + * # %`) are used to represent different visual intensities.
- `print(char, end='')` is used to print characters on the same line.
- After completing one row, a new line is printed to move to the next row.

This logic creates an ASCII image directly in the terminal.

---

## 3.How to Run the Program

### (i) Requirements
- Python 3.x installed on your system

### (ii) Steps to Run
```bash
python ascii_art.py
