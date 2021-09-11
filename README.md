# Sudoku 🧩

## Table of Contents
- [Abstract](#Abstract)
- [How To Use](#how-to-use)
- [References](#references)
- [Author(s)](#author-info)

## Abstract

The classic Sudoku game involves a grid of 81 squares. The grid is divided into nine blocks, each containing nine squares.

The rules of the game are simple: each of the nine blocks has to contain all the numbers 1-9 within its squares. Each number can only appear once in a row, column or box.

The difficulty lies in that each vertical nine-square column, or horizontal nine-square line across, within the larger square, must also contain the numbers 1-9, without repetition or omission.

This python file allows the users to solve any sudoku puzzle as well as recieve a sudoku puzzle based on selected difficulty.

## How To Use

### Installation
```
    chmod +x sudoku.py
    ./sudoku.py
```
### Puzzle
The program will prompt the user for their desired level of difficulty. It will display a random puzzle and allow the user to get the solution. If no is selected, a time will be displayed for how long the user has been working on the puzzle.
```
Problem:
 - - - - - - - - - - - - - - - -
 |  0 0 0  |  0 0 0  |  0 6 0  |
 |  0 8 0  |  5 3 6  |  0 0 9  |
 |  0 6 0  |  4 0 0  |  0 0 8  |
 - - - - - + - - - - + - - - - -
 |  0 0 0  |  2 0 3  |  8 0 0  |
 |  2 7 3  |  8 0 0  |  0 1 6  |
 |  0 0 0  |  1 0 0  |  0 0 0  |
 - - - - - + - - - - + - - - - -
 |  0 1 6  |  9 4 0  |  0 8 0  |
 |  4 2 7  |  0 8 1  |  9 0 0  |
 |  8 5 9  |  3 0 2  |  6 4 1  |
 - - - - - - - - - - - - - - - -
Would you like to see the Solution? (yes/no): no
Good Luck!, it has been: 0:25:53
Would you like to see the Solution? (yes/no): yes
Solution:
 - - - - - - - - - - - - - - - -
 |  9 3 1  |  7 2 8  |  4 6 5  |
 |  7 8 4  |  5 3 6  |  1 2 9  |
 |  5 6 2  |  4 1 9  |  3 7 8  |
 - - - - - + - - - - + - - - - -
 |  1 4 5  |  2 6 3  |  8 9 7  |
 |  2 7 3  |  8 9 4  |  5 1 6  |
 |  6 9 8  |  1 5 7  |  2 3 4  |
 - - - - - + - - - - + - - - - -
 |  3 1 6  |  9 4 5  |  7 8 2  |
 |  4 2 7  |  6 8 1  |  9 5 3  |
 |  8 5 9  |  3 7 2  |  6 4 1  |
  - - - - - - - - - - - - - - - -
Nice Job!, It took you 0:25:54 to complete the puzzle.
Would you like another puzzle? (yes/no): 
```
### Solver
Users are to input their given puzzle from left to right starting from the first row. If any mistakes were to happen, the user will have to reinput their puzzle from the beginning. 

```
Please input number in row  9 and column  9 (type 'res' to restart or 'quit' to exit)
1
 - - - - - - - - - - - - - - - -
 |  0 0 0  |  0 0 0  |  0 6 0  |
 |  0 8 0  |  5 3 6  |  0 0 9  |
 |  0 6 0  |  4 0 0  |  0 0 8  |
 - - - - - + - - - - + - - - - -
 |  0 0 0  |  2 0 3  |  8 0 0  |
 |  2 7 3  |  8 0 0  |  0 1 6  |
 |  0 0 0  |  1 0 0  |  0 0 0  |
 - - - - - + - - - - + - - - - -
 |  0 1 6  |  9 4 0  |  0 8 0  |
 |  4 2 7  |  0 8 1  |  9 0 0  |
 |  8 5 9  |  3 0 2  |  6 4 1  |
 - - - - - - - - - - - - - - - -
The Problem:
 - - - - - - - - - - - - - - - -
 |  0 0 0  |  0 0 0  |  0 6 0  |
 |  0 8 0  |  5 3 6  |  0 0 9  |
 |  0 6 0  |  4 0 0  |  0 0 8  |
 - - - - - + - - - - + - - - - -
 |  0 0 0  |  2 0 3  |  8 0 0  |
 |  2 7 3  |  8 0 0  |  0 1 6  |
 |  0 0 0  |  1 0 0  |  0 0 0  |
 - - - - - + - - - - + - - - - -
 |  0 1 6  |  9 4 0  |  0 8 0  |
 |  4 2 7  |  0 8 1  |  9 0 0  |
 |  8 5 9  |  3 0 2  |  6 4 1  |
 - - - - - - - - - - - - - - - -
Is this correct? (yes/no): yes
The Solution:
 - - - - - - - - - - - - - - - -
 |  9 3 1  |  7 2 8  |  4 6 5  |
 |  7 8 4  |  5 3 6  |  1 2 9  |
 |  5 6 2  |  4 1 9  |  3 7 8  |
 - - - - - + - - - - + - - - - -
 |  1 4 5  |  2 6 3  |  8 9 7  |
 |  2 7 3  |  8 9 4  |  5 1 6  |
 |  6 9 8  |  1 5 7  |  2 3 4  |
 - - - - - + - - - - + - - - - -
 |  3 1 6  |  9 4 5  |  7 8 2  |
 |  4 2 7  |  6 8 1  |  9 5 3  |
 |  8 5 9  |  3 7 2  |  6 4 1  |
  - - - - - - - - - - - - - - - -
Would you like to input another puzzle? (yes/no)
```

## References
- [Minimum clues for a puzzle](https://www.technologyreview.com/2012/01/06/188520/mathematicians-solve-minimum-sudoku-problem/#:~:text=Sudoku%20fanatics%20have%20found%20numerous,lurking%20somewhere%20in%20puzzle%20space)
- [How to create a sudoku puzzle](https://www.sudokuwiki.org/sudoku_creation_and_grading.pdf)

## Author Info
#### Alexander Shen - Developer
- [LinkedIn](https://www.linkedin.com/in/shenalexw/)
- [Portfolio Website](https://shenalexw.github.io/)
