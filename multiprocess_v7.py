'''Compare running functions using multiprocessing and regular serial processing'''

import time # to measure time of execution
# instantiate pool of workers to distribute on processes/functions over processors
from multiprocessing import Pool
import os


# Find out how many processors/cores on the machine
cores = os.cpu_count()
print(f'This machine has {cores} processor cores') 

# Create a CPU bound function
def sum_square(number):
    s = 0
    for i in range(number):
        s += i*i
    return s

# Create sum_square function with multiprocessing
def sum_square_multiprocess(numbers):
    start_time = time.time()
    p = Pool()
    result = p.map(sum_square, numbers)

    p.close()
    p.join()

    # Calculate function execution time
    execution_time = time.time() - start_time
    print(f'Processing {len(numbers)} nmubers took {execution_time} time using multiprocessing')

# Create sum_squre function with no multiprocessing
def sum_square_serialprocess(numbers):
    start_time = time.time()
    result = []
    for i in numbers:
        result.append(sum_square(i))

    # Calculate funciton execution time    
    execution_time = time.time() - start_time

    print(f'Processing {len(numbers)} nmubers took {execution_time} time using serial processing')

if __name__ == '__main__':
    numbers = range(10000) # 0, 1, 2, 3, . . . .99999

    # Comparing the function execution time with and without multiprocessing
    sum_square_multiprocess(numbers)
    sum_square_serialprocess(numbers)
