"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    userinput = raw_input()
    pieces = userinput.split(' ')
    print pieces
    