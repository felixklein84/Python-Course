# Docstrings and Doctests

Docstrings are used to document functions, modules, classes, and methods.
They are governed by [PEP 257](https://www.python.org/dev/peps/pep-0257/).

## One-liner

```python
def example_function():
    """This function prints example."""
    print("example")
```

Note: triple quotes are used even for one-liners.

There are different docstring styles — this course uses the [Google Docstring Guide](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

## Full Documentation

For more complex or exported functions, a detailed docstring is recommended.
The following function is also available as a [Python file](07_docstring_test.py).

```python
def dichte(x: float, mean: float = 0, variance: float = 1, log: bool = False):
    """
    Calculates the density of a normally distributed random variable.

    Given the mean and the variance this function uses numpy to return the
    density of a normally distributed random variable or the logarithm of it.
    The default arguments are set to the density of the normal distribution.

    Args:
        mean:
            Default 0. mean parameter of random variable
        variance:
            Default 1. variance parameter of random variable. Must be positive.
            Be aware that the variance is the standarddeviation squared.
        log:
            Default False. If True, the log density (log likelihood) is
            returned.

    Returns:
        The (log of the) density as float.

    Examples:
        Examples should be written in the doctest format and should illustrate
        how to use the function.
        >>> dichte(0)
        0.3989422804014327
        >>> dichte(0, log=True)
        -0.9189385332046727
        >>> dichte(0.5, mean=1, variance=2**2)
        0.19637862681301155
        >>> dichte(x=0, variance=0)
        Traceback (most recent call last):
        ...
        Exception: Variance must be positive
    """
    if variance <= 0:
        raise Exception("Variance must be positive")

    density = (
        1
        / np.sqrt(2 * np.pi * variance)
        * np.exp(-0.5 * (x - mean) ** 2 / (2 * variance))
    )

    if log:
        density = np.log(density)

    return density
```


## Doctest

The examples in docstrings can be used directly as tests:

```shell
(.venv)> python -m doctest -v lec06/07_docstring_test.py
...
4 passed and 0 failed.
Test passed.
```
