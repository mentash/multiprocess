
import time
import concurrent.futures


""" 
Measuring Code Performance Using perf_counter(). 
Place perf_counter() before and after code execution:
"""


def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return ('Done Sleeping...')
    

if __name__ == '__main__':
    # print ("Executed when invoked directly")

    start = time.perf_counter()

    #
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Schedule a function for execution and returns a future object
        
        f1 = executor.submit(do_something, 1)
        f2 = executor.submit(do_something, 1)
        print(f1.result())
        print(f2.result())

        
    end = time.perf_counter()

    execution_time = (end - start)

    print(f'Finished in {round(execution_time, 2)} second(s)')

else:
    print ("Executed when imported")
