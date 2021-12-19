
import time
import multiprocessing
#import do_something

""" 
Measuring Code Performance Using perf_counter(). 
Place perf_counter() before and after code execution:
"""


def do_something(seconds):
    print('Sleeping 1 second...')
    time.sleep(seconds)
    print('Done Sleeping...')

if __name__ == '__main__':
    # print ("Executed when invoked directly")

    start = time.perf_counter()

    # Create a list of processes
    processes = []
    
    for _ in range(10):
        # Create process(es) object(s)
        p = multiprocessing.Process(target=do_something, args=[1.5])
        # Run the process
        p.start()
        # Append each process to the list
        processes.append(p)

    for process in processes:
        # Blocks exectution on main process unitll this process terminates.
        process.join()
        
    end = time.perf_counter()

    execution_time = (end - start)

    print(f'Finished in {round(execution_time, 2)} second(s)')

else:
    print ("Executed when imported")
