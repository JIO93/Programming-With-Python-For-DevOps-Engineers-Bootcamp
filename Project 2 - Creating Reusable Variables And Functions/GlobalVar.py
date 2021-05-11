#Adding a variable before a function allows it to be used multiple times making it global. Line 2 contains the global variable.
name = "Javier"

def hello():
    print ('Hello' + name)

def goodbye():
    print ('Goodbye' + name)

hello()
goodbye()