import math

FILENAME = "113.txt"

def is_coprime(a, b):
    """Returns True if a and b are coprime (gcd is 1), otherwise False."""
    return math.gcd(a, b) == 1

def get_neighbors(grid, row, col):
    """Returns a list of orthogonal neighbors for a given position in the grid."""
    neighbors = []
    rows, cols = len(grid), len(grid[0])
    
    # Check above
    if row > 0:
        neighbors.append(grid[row - 1][col])
    # Check below
    if row < rows - 1:
        neighbors.append(grid[row + 1][col])
    # Check left
    if col > 0:
        neighbors.append(grid[row][col - 1])
    # Check right
    if col < cols - 1:
        neighbors.append(grid[row][col + 1])
    
    return neighbors

def validate_grid(grid):
    """Validates that all orthogonal neighbors in the grid are coprime."""
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            num = grid[row][col]
            neighbors = get_neighbors(grid, row, col)
            for neighbor in neighbors:
                if not is_coprime(num, neighbor):
                    print(f"Invalid pair found: {num} and {neighbor} at ({row}, {col})")
                    return False
    print("The grid is valid.")
    return True

def read_grid_from_file(filename):
    """Reads a grid from a file, assuming space-separated integers."""
    with open(filename, 'r') as f:
        grid = []
        for line in f:
            # Remove brackets and split by space to form the row
            row = list(map(int, line.strip().replace('[', '').replace(']', '').split()))
            grid.append(row)
    return grid

if __name__ == "__main__":
    # Read the grid from 'input.txt'
    grid = read_grid_from_file(FILENAME)
    
    # Validate the grid
    validate_grid(grid)
