#Specifying types isn't commonly seen in Python as Python does not make you statically type.

#In the line below we define the subtraction function. We specify that Five and ten are integers and that the result should be an integer as well.
def subtraction(five: int, ten: int) -> int:
    print (ten - five)

subtraction(10, 5)