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
