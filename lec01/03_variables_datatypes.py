"""
Learning Objective:
Overview of possible variable names, their types, and properties

Duration:
20 minutes
"""

################################################################################

# - Variables can be understood as drawers 
#   in which values are stored
# - Python does not have a command to declare variables
# - Variables are created when they are assigned a value


age = 19
name = "Max"
print(age)
print(name)


# Variables are not created with a specific type and can 
# change their type even after being defined

age = 20
name = "Martina"

name = 123


################################################################################

# Variable names
# - Variables should have SHORT but MEANINGFUL names
# - Variable names must begin with a letter or underscore ("_")
# - Variable names must not begin with a number
# - Variable names may only contain letters, numbers, and underscores
# - Variable names are case-sensitive

# Examples
_ = 1
_age = 35
hello_this_is_a_long_text = 5
age2 = 3


# What is not allowed?
"""
2age = 25
price€ = 5
hello-this-is-a-long-text = 5
first_name last_name = "Max Mustermann"
"""

# Assign multiple variables at once
x, y, z = 1, 2, 3
print(x + y + z)

a = b = 5
print(a)
print(b)
a = 3
print(b)

################################################################################

# Output variables

a = "Today is "
b = "Tuesday"
c = " and "
d = 19
e = 20
f = " o'clock"

# Concatenate strings
print(a + b)
# Add numbers
print(d + e)
# Mixing types gives an error
print(a + b + c + d + f)

# But there is a solution - fstrings
print(f"{a}{b}{c}{d}{e}{f}")



###############################################################################

# Variable types

"""
Overview of all data types.
The most relevant ones for us at the beginning are marked with *
 - Text: 
    *- str (Strings)
 - Numbers: 
    *- int (whole numbers)
    *- float (floating point numbers)
     - complex (complex numbers)
 - Logical truth values:
    *- bool (true / false)

 - Sequences
    *- list (ordered collection of elements)
     - tuple (ordered collection of elements)
     - range (increasing sequence of numbers with equal intervals)
 - Mappings
    *- dict (dictionary mapping name -> description)
     - set (unordered collection of elements)
     - frozenset (unordered collection of elements)

 - Binary data types
     - bytes
     - bytearray
     - memoryview
"""
    
# Examples for the *-cases

# Text
x = "University of Mannheim"
type(x)

# Numbers
a = 3
type(a)

b = 3.5
type(b)

c = 3.0
type(c)

# Casting for explicit assignment
d = int(3.0)
type(d)

e = int(3.5)
type(e)

f = int("2")
type(f)

g = str(3)
type(g)


# Logical truth values

w = True
f = False
type(w)
print(bool(1))
print(bool(0))
# empty texts, brackets like (), 0, None and False evaluate to false
# everything else evaluates to true
print(bool("Text"))
print(bool(None))

# List
weekdays = ["mo", "tu", "we", "th", "fr", "sa", "su"]
type(weekdays)
print(weekdays[0])



# Dictionaries
weekdays = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday",
            5: "Friday", 6: "Saturday", 7: "Sunday"}

print(weekdays[6])

degree_programs = {
   "Wifo": "Business Informatics", 
   "Wima": "Business Mathematics",
   "BWL": "Business Administration",
   "MMDS": "Mannheim Master in Data Science"
   }

print(degree_programs["BWL"])
