import string
import numpy as np
from random import choice
import itertools

class KillerSudokuSolver(object):
    def __init__(self, cages):
        self.grid_size = 4
        self.cages = cages
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)

    def generate_initial_state(self):
        for cage, target_sum in self.cages:
            cage_size = len(cage)
            possible_inputs = []

            if cage_size == 2:
                for i in range(1, 5):
                    for j in range(i + 1, 5):
                        if i + j == target_sum:
                            possible_inputs.append((i, j))
            elif cage_size == 3:
                for permutation in itertools.permutations(range(1, 5), cage_size):
                    if sum(permutation) == target_sum:
                        possible_inputs.append(permutation)
                if not possible_inputs and target_sum == 5:
                    possible_inputs.append((1, 3, 1, 3, 2, 2))
            elif cage_size == 4:
                for i in range(1, 5):
                    for j in range(i + 1, 5):
                        for k in range(j + 1, 5):
                            for l in range(k + 1, 5):
                                if i + j + k + l == target_sum:
                                    possible_inputs.append((i, j, k, l))
            #checking
            #print("Cage:", cage)
            #print("Target Sum:", target_sum)
            #print("Possible Inputs:", possible_inputs)
            if possible_inputs:
                cage_numbers = choice(possible_inputs)
                for idx, cell in enumerate(cage):
                    self.grid[cell[0] - 1, cell[1] - 1] = cage_numbers[idx]
            else:
                raise ValueError("No valid combinations for cage:", cage)

    def solve_with_simulated_annealing(self, max_iterations=5000, max_retries=100):
        temperature = 1.0
        cooling_rate = 0.99

        self.generate_initial_state()

        print("\nSimulated Annealing is running...")

        while max_iterations > 0:
            for _ in range(max_retries):
                cage_to_swap = choice(self.cages) # Randomly select a cage to swap numbers
                self.swap_numbers_in_cage(cage_to_swap[0]) # Swap numbers in the selected cage

                if self.is_valid_solution():
                    return True

            temperature *= cooling_rate
            max_iterations -= 1
        print("Simulated Annealing finished.")

        return False

    def swap_numbers_in_cage(self, cage):
        cage_values = [self.grid[cell[0] - 1, cell[1] - 1] for cell in cage]
        np.random.shuffle(cage_values)
        for idx, cell in enumerate(cage):
            self.grid[cell[0] - 1, cell[1] - 1] = cage_values[idx]

    def is_valid_solution(self):
        for i in range(self.grid_size):
            if len(set(self.grid[i, :])) != self.grid_size or len(set(self.grid[:, i])) != self.grid_size:
                return False
        return True

    def view_results(self):
        for row in range(self.grid_size):
            if row % 2 == 0:
                print("=" * 13)
            for col in range(self.grid_size):
                if col % 2 == 0:
                    print("|", end=" ")
                print(self.grid[row, col], end=" ")
            print("|")
        print("=" * 13)

def convert_to_letter(row, col):
    alphabet = string.ascii_uppercase
    return alphabet[row] + alphabet[col]

def is_grouping_valid(user_groupings):
    valid_entries = []

    for group, target_sum in user_groupings:
        try:
            target_sum = int(target_sum)
        except ValueError:
            print("Error: Target sum must be an integer.")
            return []

        if 3 <= target_sum <= 10:
            if len(group) < 2 or len(group) > 4:
                print("Error: Each grouping must have between 2 and 4 pairs.")
                return []
            if any(len(pair) != 2 for pair in group):
                print("Error: Each pair in a grouping must contain exactly 2 numbers.")
                return []
            if len(set(group)) != len(group):
                print("Error: Each cell in a grouping must be unique.")
                return []
            valid_entries.append((group, target_sum))
        else:
            print("Error: Target sum for each grouping must be between 3 and 10.")
            return []

    if len(valid_entries) < 5 or len(valid_entries) > 7:
        print("Error: You need to enter between 5 and 7 groupings.")
        return []

    return valid_entries

print("Killer Sudoku Solver using Simulated Annealing")
print("Enter 'DONE' when finished.")

user_groupings = []
while True:
    row_input = input("Enter your desired groupings separated by commas (e.g., 1,1 2,1 3,1): ").strip()

    if row_input.upper() == 'DONE':
        if len(user_groupings) >= 5 and len(user_groupings) <= 7:
            break
        else:
            print("Error: You need to enter between 5 and 7 groupings.")
            continue
    try:
        # Parse the input to extract row numbers
        rows = [tuple(map(int, pair.split(','))) for pair in row_input.split()]
        # Check if any pair contains more than 2 numbers
        if any(len(pair) != 2 for pair in rows):
            print("Error: Each pair in a grouping must contain exactly 2 numbers.")
            continue
        # Check if any row number is repeated within a group
        if len(set(rows)) < len(rows):
            print("Error: Row numbers should not be repeated within a group. Please try again.")
            continue
        # Check if any row number is outside the valid range (1 to 4)
        if any(row[0] < 1 or row[0] > 4 or row[1] < 1 or row[1] > 4 for row in rows):
            print("Error: Invalid row number. Please enter row numbers between 1 and 4.")
            continue
        # Check if any cell in the group is already included in previous groupings
        if any(any(cell in prev_group for prev_group, _ in user_groupings) for cell in rows):
            print("Error: Some cells are already included in previous groupings. Please try again.")
            continue
        # Check if there is only one pair in the grouping
        if len(rows) == 1:
            print("Error: Each grouping must contain at least two pairs.")
            continue
        target_sum = input("Enter the target sum for this group (3 to 10): ").strip()
        user_groupings.append((rows, target_sum))
    except Exception as e:
        print("Invalid input. Please try again.")

if len(user_groupings) < 5 or len(user_groupings) > 7:
    print("\nError: You need to enter between 5 and 7 groupings.")
else:
    print("\nGroupings accepted.")

valid_entries = is_grouping_valid(user_groupings)
print("\nEntered Groupings: ",valid_entries) #checking

# Initialize empty grid representing the 4x4 Killer Sudoku board
grid = [['-' for _ in range(4)] for _ in range(4)]

for i, (group, _) in enumerate(valid_entries, start=1):
    letter = chr(65 + i)
    for row, col in group:
        grid[row - 1][col - 1] = letter

print("\nKiller Sudoku Grid using Letters as Representations: ")
for row in grid:
    print(row)

killer_sudoku = KillerSudokuSolver(valid_entries)
killer_sudoku.generate_initial_state()
print("\nGenerated Initial State: ")
killer_sudoku.view_results()

if killer_sudoku.solve_with_simulated_annealing(max_iterations=5000):
    print("\nSolution found:")
    killer_sudoku.view_results()
else:
    print("\nUnable to find a solution.")
