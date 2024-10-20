import time
import numpy as np
from math import gcd


def factors(n) -> set[set[int]]:
    """
    Returns a set of factors each integer 1...n
    """
    factors = {i: set() for i in range(1, n + 1)}
    for i in range(1, n+1):
        for factor in range(1, int(i ** 0.5) + 1):
            if i % factor == 0:
                factors[i].add(factor)
                if factor != i // factor:
                    factors[i].add(i // factor)
    return factors


def num_of_factors(n) -> set[set[int]]:
    """
    Returns number of factors of each integer 1...n
    """
    factorlist = factors(n)
    num_factors = {i: len(factorlist[i]) for i in range(1, n + 1)}
    return num_factors


def most_factors_first(n) -> list[list[int]]:
    """
    Returns a list of integers sorted backwards by how many factors they have.
    This function helps bias generate_prime_grid by trying to choose to get rid of the
    "worst" numbers as early as possible, similar to move ordering in chess:
    https://www.chessprogramming.org/Move_Ordering

    An example of this in a 90x90 grid: *7560*, with 64 factors, would be
    chosen first for the top left corner of the grid.
    """
    factor_counts = num_of_factors(n)
    sorted_list = sorted(factor_counts.items(), key=lambda item: item[1], reverse=True)
    return [item[0] for item in sorted_list]


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


def is_valid(matrix, i, j, num):
    """Check if num is coprime with all its orthogonal neighbors."""
    neighbors = get_neighbors(i, j, matrix.shape[0], matrix.shape[1])
    return all(gcd(num, matrix[ni, nj]) == 1 for ni, nj in neighbors if matrix[ni, nj] != 0)


def generate_prime_grid(n, m) -> list[list[int]]:
    """
    Backtracking approach that uses most_factors_first to try to place factor-heavy numbers
    in the beginning to prevent impossible states later.
    """
    print(f"Generating {n}x{m} grid ({n*m} values)")
    grid = np.zeros((n, m), dtype=int)
    sorted_numbers = most_factors_first(n * m)
    stack = []
    index = 0

    while index < n * m:
        row, col = divmod(index, m)
        placed = False
        tried_numbers = set()

        for num in sorted_numbers:
            if num not in tried_numbers and is_valid(grid, row, col, num):
                grid[row, col] = num
                stack.append((index, num))
                sorted_numbers.remove(num)
                placed = True
                break
            tried_numbers.add(num)

        if placed:
            index += 1
        else:
            if not stack:
                return None
            # Backtrack startin from here
            while stack:
                prev_index, prev_num = stack.pop()
                row, col = divmod(prev_index, m)
                grid[row, col] = 0
                sorted_numbers.append(prev_num)
                tried_numbers.add(prev_num)
                index = prev_index
                if len(tried_numbers) < len(sorted_numbers):
                    break
            else:
                return None
    # If the placement of all numbers is valid, return the grid
    return grid if index == n * m else None
