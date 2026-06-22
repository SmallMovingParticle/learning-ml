from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(numbers):
    time.sleep(1)
    return f"numbers: {numbers}"


numbers = [1,2,3,4,5,6,6,7]

with ThreadPoolExecutor(max_workers=3) as executor:
    result=executor.map(print_numbers, numbers)

for result in result:
    print(result)