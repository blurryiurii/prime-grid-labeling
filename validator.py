import numpy as np
from math import gcd
import re

FILENAME = "grids/grid-61x61.txt"

# Function to get orthogonal neighbors
def get_neighbors(i, j, rows, cols):
    """Get the orthogonal neighbors of (i, j)."""
    neighbors = []
    if i > 0:  # Up
        neighbors.append((i - 1, j))
    if i < rows - 1:  # Down
        neighbors.append((i + 1, j))
    if j > 0:  # Left
        neighbors.append((i, j - 1))
    if j < cols - 1:  # Right
        neighbors.append((i, j + 1))
    return neighbors

# Function to check if a number is coprime with its orthogonal neighbors
def is_valid(grid, i, j, num):
    """Check if num is coprime with all its orthogonal neighbors."""
    neighbors = get_neighbors(i, j, grid.shape[0], grid.shape[1])
    return all(gcd(num, grid[ni, nj]) == 1 for ni, nj in neighbors if grid[ni, nj] != 0)

# Function to parse the input file
def parse_grid_file(filename):
    """Parse the grid from a formatted file."""
    grid = []
    with open(filename, 'r') as f:
        grid = [[int(v) for v in re.split(r"\s+", m.group(1))] for m in re.finditer(r"\[\s*((?:\d+\s*)+)\]", f.read())]
        print(grid)
        for line in f:
            # Strip brackets and split into numbers
            line = line.strip().replace('[', '').replace(']', '')
            if line:
                row = list(map(int, line.split()))
                grid.append(row)

    return np.array(grid)

# Function to validate the entire grid
def validate_prime_labeled_grid(filename):
    """Validate that all orthogonal neighbors in the grid are coprime."""
    grid = parse_grid_file(filename)
    rows, cols = grid.shape
    for i in range(rows):
        for j in range(cols):
            if not is_valid(grid, i, j, grid[i, j]):
                print(f"Validation failed at ({i}, {j}) with value {grid[i, j]}")
                return False
    print("The grid is valid: All orthogonal neighbors are coprime.")
    return True

# Example usage
validate_prime_labeled_grid(FILENAME)
