import numpy as np
from math import gcd


def factors_set(n) -> set[set[int]]:
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


def num_of_factors_set(n) -> set[set[int]]:
    """
    Returns number of factors of each integer 1...n
    """
    factors = factors_set(n)
    num_factors = {i: len(factors[i]) for i in range(1, n + 1)}
    return num_factors


def sorted_num_of_factors(n) -> list[list[int]]:
    """
    Returns a list of integers sorted backwards by how many factors they have.
    This function helps bias generate_prime_grid by trying to choose to get rid of the
    "worst" numbers as early as possible, similar to move ordering in chess:
    https://www.chessprogramming.org/Move_Ordering

    An example of this in a 90x90 grid: *7560*, with 64 factors, would be
    chosen first for the top left corner of the grid.
    """
    factor_counts = num_of_factors_set(n)
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
    grid = np.zeros((n, m), dtype=int)
    sorted_numbers = sorted_num_of_factors(n * m)
    
    def backtrack(index):
        if index == len(sorted_numbers):
            return True
        
        num = sorted_numbers[index]
        
        for i in range(n):
            for j in range(m):
                if grid[i, j] == 0 and is_valid(grid, i, j, num):
                    grid[i, j] = num  # Place number
                    if backtrack(index + 1):  # Recur for the next number
                        return True
                    grid[i, j] = 0  # Backtrack
            
        return False
    
    if backtrack(0):
        return grid.tolist()
    return None


# Example usage
prime_grid = generate_prime_grid(10, 10)
if prime_grid is not None:
    for row in prime_grid:
        print(row)
else:
    print("Failed.")