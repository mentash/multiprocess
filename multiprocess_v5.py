
import time
import concurrent.futures


""" 
Measuring Code Performance Using perf_counter(). 
Place perf_counter() before and after code execution:
"""


def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return (f'Done Sleeping...{seconds}')
    

if __name__ == '__main__':
    # print ("Executed when invoked directly")

    start = time.perf_counter()

    #
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2 , 1]
        # run function (do_something) against every item in iterable (secs list)
        # map returns the results in the order they started -not- as completed
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

        
    end = time.perf_counter()

    execution_time = (end - start)

    print(f'Finished in {round(execution_time, 2)} second(s)')

else:
    print ("Executed when imported")
