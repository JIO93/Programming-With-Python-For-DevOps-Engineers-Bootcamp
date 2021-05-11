"""Importing the sys library allows you to create an argument and call it at runtime by running 
"Python filename argumentname" in the terminal for this script it would look like this.
"python .\RuntimeVar.py JIO" """


import sys

def hello(name):
    print ('Hello' + name)

name = sys.argv[1]

hello(name)