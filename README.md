# Python Function Bench Marker
Calculates the total time taken for a function to run on the CPU (excludes time sleeping).

### Usage

###### Example Function

```python
def my_func(x, y, repeat=False):
    total = x + y
    if repeat:
        total += x + y
    return total
```

###### Example Usage

```python
>>> bench(my_func, 1, 2, iterations=10_000_000, repeat=True)
    0.40625
>>> bench(my_func, 1, 2, output=True, iterations=1_000_000)
    Function: my_func{
        Total time taken: 0.031s
        Average time taken: 0.000s
    }
	
    0.03125
>>> 
```

--------

Information provided by this function may not be accurate.
