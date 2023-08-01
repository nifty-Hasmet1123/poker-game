# Always create this when in a project
# This helps to identify the test directory as the equivalent of a package.
# And this is going to allow us to help unit test discover all the files that we are going to place 
# inside the test directory effectively instead of telling unit tests to run. Let's say six different files, 
# were going to tell it to run a directory and it's going to find all the files within them that have tests and 
# run all the tests within those files. But in order to do that, it has to be able to recognize a directory
# And in order for it to recognize a directory as a python construct, it needs to be a package, means we need to put a 
# dundar init.py file inside it.

# So basically in order for the program to recognize the folder as a package it need a __init__.py file inside it.

# when you want to access many modules 

# example there is a module named calculator in this directory and within that calculator module there are variables
# named numbers = 45, PI = 3.14

# if you want to access that without importing that file you can place a syntax in here using the dot syntax for direct
# access. This is usable when you have plenty of modules inside a directory

# from .calculator import number, PI