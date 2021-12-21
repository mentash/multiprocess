
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
        # Loop using list comprehension to create results list
        # Submit function schedules a process for execution one at at time
        results = [executor.submit(do_something, sec) for sec in secs]
        #print(results)
        # Takes interator (results list) and yeilds the results of processes as completed
        for f in concurrent.futures.as_completed(results):
            print(f.result())

        
    end = time.perf_counter()

    execution_time = (end - start)

    print(f'Finished in {round(execution_time, 2)} second(s)')

else:
    print ("Executed when imported")
