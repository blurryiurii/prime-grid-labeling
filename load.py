import time
import sys

def loading_bar(total):
    for i in range(total + 1):
        percent = (i / total) * 100
        bar = '█' * i + '-' * (total - i)
        sys.stdout.write(f'\r|{bar}| {percent:.2f}%')
        sys.stdout.flush()
        time.sleep(0.1)  # Simulating work being done
    print()  # Move to the next line after completion

loading_bar(30)