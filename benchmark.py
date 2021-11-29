import time

def bench(func, iterations=1, *args):
    """Time how long a function takes to execute.
    Prints out the total time and the average time of the execution.

    Returns: A float of the total time taken in seconds."""
    # Type Check.
    if not isinstance(iterations, int):
        raise TypeError(f"Expected int for iterations but got {type(iterations)}")
    # Value Check. Cannot repeat less than 1 times.
    if iterations < 1:
        raise ValueError("Positive integer needed for the number of times to call the function.")

    # Information to gather from the process.
    totalTime = 0
    averageTime = 0
    start = time.time()

    # Call func n times.
    for repeat in range(iterations):
        func(*args)
    totalTime += time.time() - start

    output = f"Total time taken: {totalTime:.3f}s\n" + f"Average time: {totalTime/iterations:.3f}s\n"
