"""
Learning objective:
Quickly understand the basic syntax of Python.

Duration:
10 minutes
"""

# This is a Python file. 
# It typically ends with .py.
# Comments begin with # and apply until the end of the line.

# Output a text.
print("Good evening, Mannheim!")

# Use Python as a calculator
1 + 2
2 * (15 / 3)


# Use variables
x = 5
y = 3
z = x + y
a = "Good evening"
b = "Mannheim"

# Notes:
# - Variables are created when 
#   they are assigned a value for the first time.
# - There is no command to declare variables.


# Indentation of text is crucial in Python.

if 1 > 0:
    print("1>0 is always true, so this line is printed.")

if 0 > 1:
    print("This line is not printed because 0>1 is always false.")

# Caution 
if 0 > 1:
    print("Python throws an indentation error because \
      it expects a statement for the if block.")

# If you don't want to execute anything, you can actively avoid this
if 0 > 1:
    pass
print("Now there is no error. \
    However, this text is no longer part of the if block")