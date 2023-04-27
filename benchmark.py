from time import process_time
from sys import stdout

def bench(func, *args, iterations=1, output=False, log=stdout, **kwargs):
    """Time how long a function takes to execute.

    The time calculated only accounts for the time spent on the CPU,
    and not time spent sleeping.

    Parameters:
        func - the function to operate on
        args - arguments for the function
        interations - the number of times to run the function
        output - whether to display time information after execution
        log - writes the output to the log file if output is true
        kwargs - key word arguments for the function

    Returns:
     - A float of the total time taken in seconds.
    """
    # Type Check.
    if not isinstance(iterations, int):
        raise TypeError(
            f"Expected int for iterations but got {type(iterations)}")
    # Value Check. Cannot repeat less than 1 times
    if iterations < 1:
        raise ValueError(
            "Positive integer needed for iterations (iterations >= 1)")

    # Information to gather from the process
    total_time = 0
    average_time = 0
    start = process_time()

    # Call func n times
    for repeat in range(iterations):
        func(*args, **kwargs)
    total_time = process_time() - start
    average_time = total_time / iterations

    # Output
    if output:
        output = (f"Function: {func.__name__} \{\n"
                  + f"\tTotal time taken: {totalTime:.3f}s\n"
                  + f"\tAverage time taken: {average_time:.3f}s\n"
                  + "}\n\n")
        print(output, file=log)
    return total_time
