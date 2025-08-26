"""
# Certificate Exam 24.11.

* Exam Type: Open-Book Exam  
* Duration: 45 minutes (+15 minutes for download & upload)  
* Total Points: 45  
* Passing Score: 25 points guarantees a pass  

Submit your solution by **8:00 PM** via email to [kurse@stads.de](mailto:kurse@stads.de).

Your code must run in Python 3.8.5 with the following versions:  
- numpy 1.19.2  
- pandas 1.1.3  
- matplotlib 3.3.2  
- seaborn 0.11.0 or plotly 4.12.0  

If other packages or versions are used, you must specify the version used.

## Task 1: Basics *(18 points)*

* Create a Python file named `<Lastname>_<Firstname>_exam.py` (e.g. `kern_moritz_exam.py`) and complete this task in that file.

### Task 1a: Get Started *(2 points)*

* Define the two variables `x` and `y` as `-10` and `20` respectively *(1 point)*  
* Print the squared distance result, i.e. `(x - y)^2`. (Hint: `**`, `print`) *(1 point)*

### Task 1b: Simple Function *(6 points)*

* Define a function `abstand_quadriert` that takes the two variables `x` and `y` as input *(1 point)*  
* The function should check whether the difference between `x` and `y` is zero:  
    * If true: print `"x and y are equal."` and return `0` *(2 points)*  
    * Otherwise: return the result of `(x - y)^2` *(2 points)*  
* Evaluate the function with the input combinations `(x=5, y=5)` and `(x=4, y=6)` *(1 point)*

### Task 1c: Data Types *(6 points)*

* Create a variable `x` with value `0`. Explicitly convert `x` to a Boolean (True/False) and store the result as `z` *(1 point)*  
* Define a variable `z_is_bool` as `TRUE` if `z` is of type `bool`, otherwise `FALSE`. Hint: use `isinstance`. *(1 point)*  
* Create a dictionary named `semester` with the following mapping (each maps to a list): *(3 points)*  
    * `"FSS"` -> `["Spring-Summer Semester", "01 February"]`  
    * `"HWS"` -> `["Autumn-Winter Semester", "01 September"]`  
* Print the element with the key `"FSS"` *(1 point)*

### Task 1d: Loops *(4 points)*

* Use a for loop to generate the following output: *(4 points)*  
    ```
    1
    -2
    3
    -4
    5
    -6
    ...
    29
    -30
    ```

## Task 2: Important Packages *(27 points)*

* Create an IPython notebook named `<Lastname>_<Firstname>_exam.ipynb` (e.g. `kern_moritz_exam.ipynb`) and complete the following tasks.

### Task 2a: Numpy *(6 points)*

* Create a vector `v` that looks like: *(1 point)*  
    ```
    [2000, 2004, 2008, 2012, 2016, 2020, ..., 2092, 2096]
    ```
* Create a matrix `ma_diag` of shape (12,12) with `1`s on the diagonal and `0`s elsewhere *(1 point)*  
* Set the top-right element of the matrix (`ma_diag[0, -1]`) to `np.NaN` *(1 point)*  
* Initialize a random number generator *(1 point)*  
* Use the generator to simulate a random number `z` uniformly distributed on [0, 1] *(1 point)*  
* Replace the NaN element in the matrix with your generated value `z`  
* Compute the element-wise exponential of `ma_diag` and store the resulting matrix as `ma_diag_exp` *(1 point)*

### Task 2b: Pandas Basics *(9 points)*

You will need the dataset `activity.csv` for this task.

* Import the dataset `activity.csv` *(2 points)*  
* Display the first 10 rows *(1 point)*  
* How many rows and columns does the dataset have? *(1 point)*  
* Drop the column `country_region_code` and convert the column `date` to datetime format  
  (Hint: use `pd.to_datetime`). Save the resulting DataFrame as `df` and use it for the following tasks *(2 points)*  
* Create a new column `change_from_baseline` as the sum of  
  `retail_and_recreation_percent_change_from_baseline` and  
  `grocery_and_pharmacy_percent_change_from_baseline` *(1 point)*  
* Print the 5 rows with the **lowest** values in `change_from_baseline`.  
  What was the `change_from_baseline` on November 15, 2020 in Baden-Württemberg? *(2 points)*

### Task 2c: Pandas Advanced *(7 points)*

* Print the correlation between `retail_and_recreation_percent_change_from_baseline`  
  and `grocery_and_pharmacy_percent_change_from_baseline` *(2 points)*  
* Group the dataset by the column `Bundesland` and filter it for observations from  
  **September 1, 2020** onward. Use this filtered dataset for the next task *(2 points)*  
* Identify which federal state (`Bundesland`) had the **largest average decline** in shopping,  
  i.e. the state with the **lowest average** in `grocery_and_pharmacy_percent_change_from_baseline` *(2 points)*

### Task 2d: Plots *(6 points)*

* Group the dataset by `date` and aggregate  
  `retail_and_recreation_percent_change_from_baseline` by the mean.  
  Use this new dataset for the next task *(1 point)*  
* Create a **scatterplot** with `date` on the x-axis and  
  `retail_and_recreation_percent_change_from_baseline` on the y-axis.  
  You may use any library (e.g. pandas, matplotlib, seaborn, plotly) *(5 points)*
"""
