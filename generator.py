import time
import v4
import os

# Range of NxN grids you'd like to try generating
START_N = 1
END_N = 61

OUTPUT_FOLDER = "grids"
SUCCESS_TRACKER_FILE = OUTPUT_FOLDER + "/_successful-grids.txt"

# Create directory if it's not already there
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Meat & potatoes 
sum_start = time.perf_counter()
for i in range(START_N, END_N + 1):
    start = time.perf_counter()
    prime_grid = v4.generate_prime_grid(i, i)
    delta = round(time.perf_counter() - start, 4)

    if prime_grid is not None:
        print(f"Success! {i}x{i} grid took {delta} seconds.")
        # Save successful grids in graphs directory
        with open(f"{OUTPUT_FOLDER}/grid-{i}x{i}.txt", "w") as f:
            for row in prime_grid:
                f.write(str(row))
                f.write("\n")
            f.write("\n")
        with open(SUCCESS_TRACKER_FILE, "a+") as f:
            f.write(str(i) + "\n")
    else:
        print(f"FAILED. {i}x{i} grid took {delta} seconds.")
print(f"All done! Total: {round(time.perf_counter() - sum_start, 2)}s.")