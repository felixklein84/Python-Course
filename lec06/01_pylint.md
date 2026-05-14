# Pylint

## About pylint

`pylint` is a helpful tool that:
* checks compliance with coding standards:
    * verifies line length
    * checks variable names against naming conventions
    * detects imports of unused modules
* finds errors:
    * checks whether declared interfaces are correctly implemented
    * checks imports of used modules
    * ...
* supports refactoring

The coding standard `pylint` enforces is based on
[PEP 8](https://www.python.org/dev/peps/pep-0008/),
the style guide for Python code. "PEP" stands for "Python Enhancement Proposals".


## First Example

We create a file `lec06/02_pylint_example.py` with the following content:

```python
def quicksort(arr):
    print('I am being called right now.')
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    Left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if False:
        print("This branch is never reached")
    return quicksort(Left) + middle + quicksort(right)
```

Now we run the following command in the terminal:

```bash
(.venv)> pylint lec06/02_pylint_example.py
************* Module 02_pylint_example
lec06/02_pylint_example.py:1:0: C0114: Missing module docstring (missing-module-docstring)
lec06/02_pylint_example.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)
lec06/02_pylint_example.py:6:4: C0103: Variable name "Left" doesn't conform to snake_case naming style (invalid-name)
lec06/02_pylint_example.py:9:4: W0125: Using a conditional statement with a constant value (using-constant-test)

-------------------------------------------------------------------
Your code has been rated at 6.36/10 (previous run: 10.00/10, -3.64)
```

To understand what a specific error message means, run:

```bash
(.venv)> pylint --help-msg=missing-module-docstring
:missing-module-docstring (C0114): *Missing module docstring*
Used when a module has no docstring. Empty modules do not require a docstring.
This message belongs to the basic checker.
```
