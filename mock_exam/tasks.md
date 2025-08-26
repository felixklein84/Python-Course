"""
# Mock Exam

* Exam Type: Open-Book Exam  
* Duration: 45 minutes (+10 minutes for download & upload)  
* Total Points: 45  
* Passing Score: 25 points  

Your code must run in Python 3.8.5 with the following versions:  
- numpy 1.19.2  
- pandas 1.1.3  
- matplotlib 3.3.2  
- seaborn 0.11.0 or plotly 4.12.0  

If other packages or versions are used, you must specify the version.

## Task 1: Basics *(18 points)*

* Create a Python file named `<Lastname>_<Firstname>_mockexam.py` (e.g. `kern_moritz_mockexam.py`) and complete this task in that file.

### Task 1a: Get Started *(2 points)*

* Define two variables `a` and `b` with values `3` and `5` respectively *(1 point)*  
* Print the result of `(a - b)/(a + b)` *(1 point)*

### Task 1b: Simple Function *(6 points)*

* Define a function `berechnung` that takes variables `a` and `b` as input. *(1 point)*  
* The function should check if `a + b == 0`:  
    * If true: print `a+b must not be 0.` and return `None` *(2 points)*  
    * Otherwise, return the result of `(a - b)/(a + b)` *(2 points)*  
* Evaluate the function with the inputs `(a=0, b=0)` and `(a=1, b=2)` *(1 point)*

### Task 1c: Data Types *(6 points)*

* Create a variable `x` as a float with value `0`. *(1 point)*  
* Define a variable `x_is_float` as `TRUE` if `x` is of type `float`, otherwise `FALSE`. Hint: use the function `isinstance`. *(1 point)*  
* Create a dictionary called `farben` with the following mapping: *(3 points)*  
    * `"red"` -> `(255, 0, 0)`  
    * `"green"` -> `(0, 255, 0)`  
    * `"blue"` -> `(0, 0, 255)`  
* Print the element with the key `"green"` *(1 point)*

### Task 1d: Loops *(4 points)*

* Use a for loop to generate the following output: *(4 points)*  
    ```
    1
    12
    123
    1234
    ...
    123456789
    ```

## Task 2: Important Packages *(27 points)*

* Create an IPython notebook named `<Lastname>_<Firstname>_mockexam.ipynb` (e.g. `kern_moritz_mockexam.ipynb`) and complete the following tasks in that notebook.

### Task 2a: Numpy *(7 points)*

* Create a vector `v` that looks like: *(1 point)*  
    ```
    [0, 4, 8, 12, 16, ..., 196]
    ```
* Create a matrix `m` of shape (50,50) with `1`s on the diagonal and `0`s elsewhere. *(1 point)*  
* Set the last element in the bottom-right corner of the matrix `m` to `NA`. *(1 point)*  
* Initialize a random number generator. *(1 point)*  
* Use the generator to create a vector `z` of shape (1, 50) with independent normally distributed random variables. *(1 point)*  
* Compute the element-wise logarithm of `z` and store it as `z_log`. *(1 point)*  
* Compute the matrix product of `z_log` and `m`. *(1 point)*

### Task 2b: Pandas Basics *(9 points)*

For this task, you will need the dataset [pendler.csv](pendler.csv).

* Import the dataset using pandas. Hint: set parameters `sep=";"` and `thousands="."` *(2 points)*  
* Display the first 5 rows. *(1 point)*  
* How many rows and columns does the dataset contain? *(1 point)*  
* Drop the column `Gemeindekennziffer` and set the column `Name` as the index.  
  Save the resulting dataset and use it for the following tasks. *(2 points)*  
* Create a new column `Nettopendler` as the difference between `Einpendler` and `Auspendler`. *(1 point)*  
* Display the top 5 cities with the highest `Nettopendler`.  
  How many net commuters does Mannheim have? *(2 points)*

### Task 2c: Pandas Advanced *(6 points)*

* Create a new column `Einpendlerquote` by dividing `Einpendler` by `Erwerbstaetige_am_Arbeitsort`. *(1 point)*  
* Compute the correlation between `Erwerbstaetige_am_Arbeitsort` and `Einpendlerquote`. *(2 points)*  
* Filter the dataset for cities with at least 10,000 employed people at the workplace.  
  Which city has the highest `Einpendlerquote` and what is the value? *(3 points)*

### Task 2d: Plots *(5 points)*

* Create a scatter plot with `Einpendler` on the x-axis and `Auspendler` on the y-axis.  
  You may use any package you prefer (e.g. pandas, matplotlib, seaborn, plotly). *(5 points)*

"""
