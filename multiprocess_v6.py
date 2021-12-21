
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


if __name__ == '__main__':
    numbers = range(5) # 0, 1, 2, 3, 4
    p = Pool()
    # Map list of variables to run in a function
    result = p.map(sum_square, numbers)
    print(result)

    p.close()
    p.join()

