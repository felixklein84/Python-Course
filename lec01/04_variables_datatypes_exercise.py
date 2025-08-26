"""
Learning Objective:
Deepen understanding of typical variable names, their types, and properties

Duration:
5 minutes self-study time
5 minutes discussion
"""


################################################################################
# Task 1
# - Reformat the following variables so that they are valid variable names

name_university = "Mannheim"
today_is_tuesday = True
year_2020 = "current year"
value_in_percent = 0.01




################################################################################
# Task 2
# - Assign the number 2020 as an integer value to the variable x

x = 2020

# - Assign the number 2020 to x in another way as an integer value

x = int("2020")

# - Output the text "x is of int type" if x is of type int

if type(x) == int:
    print("x is of int type")

# - a is defined as follows. Define b with the same value as a 
#   but as an integer
a = "68131"
b = int(a)

# - Define c with the same value as a but as a float

c = float(a)



################################################################################
# Task 3
# - Create a list with the buildings Schloss, A3, A5, B6 as elements

buildings = ["Schloss", "A3", "A5", "B6"]

# - Create a dictionary where the keys are the grades 1.0, 2.0, 
#   3.0, 4.0 and map them to "very good", "good", "satisfactory",
#   "sufficient"

grades = {
    1.0: "very good",
    2.0: "good",
    3.0: "satisfactory",
    4.0: "sufficient"
}

# - Output the first element of the above list – i.e., Schloss

print(buildings[0])

# - Output the verbal grade corresponding to 4.0

print(grades[4.0])
