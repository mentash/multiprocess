import multiprocessing
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

if __name__ == '__main__':
    # Create process(es) object(s)
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    # Start running process
    p1.start()
    p2.start()

    # Blocks the execution of the main process until the process whose join method is called terminates. 
    p1.join()
    p2.join()

end = time.perf_counter()

execution_time = (end - start)

print(f'Finished in {round(execution_time, 2)} second(s)')

