#################################
# Python Pocket Card - 01 Code #
#################################

# Reference
# PEP-8 Style Guides https://peps.python.org/pep-0008/ 
#                    https://realpython.com/python-pep8/#naming-conventions  

#######################
# 00 - Commentaries
#######################

# Single-line Commentaries 

# Multi-line commetaries
# with the hash mark. 


""" Single line Docstring Comment """

""" Multi-line Docstring Comment
    Note: the autoDocstring VSCode extension can be used 
          to automatically generate docstrings
"""

#######################
# 01 Basic Data Types 
#######################

boolean_one = True
boolean_two = False
boolean_three = bool(True)

integer_one = 33
integer_two = 30594
integer_three = int(4930)

float_one = 30.3
float_two = 4930.45
float_three = float(458.78)

complex_number_one = 2 + 3j
complex_number_one = complex(3 + 2j)

string_one = "Jonesy"
string_two = 'Ramirez'
string_three = "Hello, Select your character!"
string_four = str(string_two + ", " + "Game Over!")

#######################
# 01 Functions  
#######################
 
def check_variable_type(variable_to_check): 
    """ Function to check any variable type, with one argument (variable_to_check) """ 
    return type(variable_to_check)

# Function Calls
print(check_variable_type(boolean_two))
print(check_variable_type(boolean_two))
print(check_variable_type(float_one))
print(check_variable_type(string_three))

# Print the docstring
print(check_variable_type.__doc__)