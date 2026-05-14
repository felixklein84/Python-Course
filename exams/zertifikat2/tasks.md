# Certificate Exam 30.01.2021

* Exam Type: Open-Book Exam
* Duration: 45 minutes (+ 15 minutes for download & upload)
* Total Points: 45
* Passing Score: 25 points guarantees a pass

Submit your solution by **11:00 AM** via email to [kurse@stads.de](mailto:kurse@stads.de).

Your code must run in Python 3.8.5 with the following versions: numpy 1.19.2, pandas 1.1.3, matplotlib 3.3.2, seaborn 0.11.0 or plotly 4.12.0. If other packages or versions are used, you must specify the version.

In this exam, `x^y` denotes x raised to the power of y. For example, `3^4` means 3 to the power of 4, i.e. `3*3*3*3=81`.

## Task 1: Basics *(18 points)*

* Create a Python file named `<Lastname>_<Firstname>_exam.py` (e.g. `kern_moritz_exam.py`) and complete this task in that file.

### Task 1a: Get Started *(2 points)*

* Consider a right triangle with sides a, b, and c.
  Define variables `b` and `c` as `4` and `5` respectively. *(1 point)*
* Print the missing leg of the triangle, i.e. `(c^2 - b^2)^(1/2)`. (Hint: `**`, `print`) *(1 point)*

### Task 1b: Simple Function *(6 points)*

* Define a function `pythagoras` that takes two variables `b` and `c` as input. *(1 point)*
* The function should check whether `c^2` is less than `b^2`:
    * If true: print `c^2 must be greater than or equal to b^2.` and return `0`. *(2 points)*
    * Otherwise: return the result of `(c^2 - b^2)^(1/2)`. *(2 points)*
* Evaluate the function with inputs `(b=12, c=13)` and `(b=24, c=7)`. *(1 point)*

### Task 1c: Data Types *(6 points)*

* Create a variable `z` with value `1`. Explicitly convert `z` to a Boolean (True/False) and store the result as `a`. *(1 point)*
* Define a variable `z_is_is_bool` as `TRUE` if `z` is of type `bool`, otherwise `FALSE`. Hint: use `isinstance`. *(1 point)*
* Create a dictionary named `vaccination_status` with the following string mapping: *(3 points)*
    * `"--"` -> `"Both are vaccinated."`
    * `"-+"` -> `"Only the transmitter is vaccinated."`
    * `"+-"` -> `"Only the recipient is vaccinated."`
    * `"++"` -> `"Neither is vaccinated."`
* Print the element with key `"+-"`. *(1 point)*

### Task 1d: Loops *(4 points)*

* Use a for loop to generate the following output (written out in full): *(4 points)*
    ```
    1
    22
    4444
    88888888
    16161616161616161616161616161616
    32323232...32
    64646464646464...64
    ```

## Task 2: Important Packages *(27 points)*

* Create an IPython notebook named `<Lastname>_<Firstname>_exam.ipynb` (e.g. `kern_moritz_exam.ipynb`) and complete the following tasks in that notebook.

### Task 2a: NumPy *(6 points)*

* Create a vector `v` of 8 equally spaced points on the closed interval [0, 1], i.e.: *(1 point)*
    ```
    [0, 0.1428, 0.2857, 0.4285, 0.5714, 0.7142, 0.8571, 1]
    ```
* Initialize a random number generator. *(1 point)*
* Use the generator to simulate two vectors `U` and `V`, each with 1000 independent uniformly distributed random numbers on [0, 1]. *(1 point)*
* Compute the element-wise vector Z as `(-2 * log(U))^(-1/2) * cos(2 * pi * V)`. (Hint: `np.log`, `np.cos`, `np.pi`, `np.sqrt`) *(2 points)*
* Print the mean and variance of Z. *(1 point)*

### Task 2b: Pandas Basics *(9 points)*

For this task, you will need the dataset [election.csv](election.csv).

* Import `election.csv` and store it as `df`. *(2 points)*
* Display the first 10 rows. *(1 point)*
* How many rows and columns does the dataset contain? *(1 point)*
* Create a new column `relative_votes` as the ratio of `candidatevotes` to `totalvotes`. *(1 point)*
* How many votes did Donald Trump and Joe Biden each receive in Texas in the 2020 election? *(2 points)*
* Which candidate received the most `relative_votes` in a single state election? Also report the state and year. *(2 points)*

### Task 2c: Plots *(6 points)*

* Filter `df` for Democratic Party results in Delaware. *(1 point)*
* Create a scatter plot with the election year on the x-axis and `relative_votes` on the y-axis.
  This shows the Democratic vote share in Delaware over time.
  You may use any package (e.g. pandas, matplotlib, seaborn, plotly). *(5 points)*

### Task 2d: Pandas Advanced *(7 points)*

* Group the dataset by `year` and identify in which year the most total votes were cast. *(2 points)*
* Group by `year` and `party_simplified` and aggregate by summing rows. Store the result as `df_agg`. *(2 points)*
* Create a new column `relative_votes_agg` as the ratio of the summed `candidatevotes` to `totalvotes` in `df_agg`. *(1 point)*
* Which party received the highest percentage of votes across all available years? Also report the election year and vote share. *(2 points)*

## Submission

Send **both** files you created to [kurse@stads.de](mailto:kurse@stads.de) before the deadline (11:00 AM).
