# Killer-Sudoku-using-Simulated-Annealing
Machine Problem 2 in the course Artificial Intelligence.

This Python program solves Killer Sudoku puzzles using simulated annealing. Killer Sudoku is a variant of traditional Sudoku, with additional constraints on the sum of numbers within certain groups called "cages."

## Features

- <font size="4">Generates initial states for Killer Sudoku puzzles.</font>
- <font size="4">Implements simulated annealing algorithm to solve the puzzles.</font>
- <font size="4">Provides a visual representation of the solved puzzle.</font>

## Local Constraints

- <font size="4">The sum of numbers within each grouping should be equal to the specified target sum.</font>
- <font size="4">Each grouping must contain between 2 and 4 pairs.</font>
- <font size="4">Each pair in a grouping must contain exactly 2 numbers.</font>
- <font size="4">All numbers within a grouping must be unique.</font>

## Global Constraint

- <font size="4">Each subgrid in a 4x4 Killer Sudoku puzzle should contain numbers 1 through 4.</font>
- <font size="4">Each row and column should contain numbers 1 through 4 without repetition.</font>

## How to Use

1. Run the Python script `killer_sudoku_solver.py`.
2. Input the desired groupings separated by commas (e.g., `1,1 2,1 3,1`).
3. Enter the target sum for each grouping (3 to 10).
4. The program will generate an initial state and attempt to solve the puzzle using simulated annealing.
5. If a solution is found, it will be displayed; otherwise, the program will indicate that no solution was found.

