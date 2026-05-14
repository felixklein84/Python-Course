# Code Formatting with Black

`black` is an automatic code formatter that reformats code according to a subset of the PEP 8 standard.

Install `black` via `poetry add black` or `pip install black`.


## Example

We save the following code as `lec06/04_black_unformatted.py`:

```python
"""
This example demonstrates Black's code reformatting.
"""

import pandas as pd; import numpy as np


def any_function(x):
    i=0
    
    while i<10:
     print(f'Current number: {i}')
     i=i=1


dictionary = {1: 'a very long string stored as a value in this dictionary',
2: np.array([[1,2,3,4,5,6], [10,11,12,13,14,15,16]]),
3: lambda x: x**3}
```

We run Black on it:

```bash
(.venv)> black lec06/04_black_unformatted.py
reformatted lec06/04_black_unformatted.py
All done! ✨ 🍰 ✨
1 file reformatted.
```

The file is overwritten with the formatted code:

```python
"""
This example demonstrates Black's code reformatting.
"""

import pandas as pd
import numpy as np


def any_function(x):
    i = 0

    while i < 10:
        print(f"Current number: {i}")
        i = i = 1


dictionary = {
    1: "a very long string stored as a value in this dictionary",
    2: np.array([[1, 2, 3, 4, 5, 6], [10, 11, 12, 13, 14, 15, 16]]),
    3: lambda x: x ** 3,
}
```

Black can also be configured as a formatter-on-save in VS Code or integrated into pre-commit hooks.
