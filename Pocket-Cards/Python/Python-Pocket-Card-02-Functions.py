###########################################
#                                         #
#    Python Pocket Card 01 Functions      #
#                                         #
#         By Yoann AMAR ASSOULINE         #
#                                         #
########################################### 

# Built-in Modules 
import os
import sys

boolean_two = True 
float_one = 34.5
string_three = "test"

player_health = 100 

#######################
# 07 Functions Basics
#######################
 
# Simple Function writing
def simple_function(): 
    """ Function Comment (Docstring) """
    print("This is a simple function")

# Simple Function Call
simple_function()

# Function with Three Arguments/ Parameters
def function_with_arguments(arg1, arg2, arg3 = "my optional argument"):
    print( "Function with arguments: " + str(arg1) + " " + str(arg2) + " " + str(arg3))

function_with_arguments("Hello", arg2="test")


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



# Example Functions 
def player_identity(): 
    """ Function to display information about the current player"""
    print("Health: " + str(player_health))
