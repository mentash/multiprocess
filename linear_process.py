import time

""" 
Measuring Code Performance Using perf_counter(). 
Place perf_counter() before and after code execution:
"""

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping')

do_something()
do_something()

end = time.perf_counter()

execution_time = (end - start)

print(f'Finished in {round(execution_time, 2)} second(s)')

