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
    totalTime = time.time() - start

    # Output.
    output = f"Function: {func.__name__}:\nTotal time taken: {totalTime:.3f}s\n" + f"Average time: {totalTime/iterations:.3f}s\n"
    print(output, end="")
    return totalTime

def compare(func1, func2, iterations=1, *args):
    """Allows you to compare to similar functions
    Both functions will be given the same arguments so they mnust be similar
    in structure.

    Runs each function based on the number of iterations given. Displays how much faster
    a function was as a percentage.

    Returns: A float of the total difference in time between the execution of the two
    functions."""
    # No need to type check or value check because it is done inside bench().
    time_func1 = bench(func1, iterations, *args)
    time_func2 = bench(func2, iterations, *args)

    sep = "------------------------------\n"
    
    # Find out which function was faster.
    if time_func1 < time_func2:
        percentage = (time_func2 / time_func1) * 100
        print(sep + f"{func1.__name__}: +{percentage:.2f}%\n", end = "")
    elif time_func1 > time_func2:
        percentage = (time_func1 / time_func2) * 100
        print(sep + f"{func2.__name__}: +{percentage:.2f}%\n", end = "")
    else: # Equal execution time.
        print(f"{func1.__name__} == {func2.__name__}")
    
    
