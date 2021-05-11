"""Method is what you call a function that is inside of a class.
Below we are specifying the Methods for our class.
"""

class Cars:
    def __init__(self, model, make, year):
        self.model = "Ford"
        self.make = make
        self.year = year

    def print_model(self):
        print(self.model)

    def print_make_and_year(self, make, year):
        print(make)
        print(year)

#Class allows us to call the functions inside of a variable. You must specify objects so they become available to use.
my_cars = Cars("Ford", "F150", "2020")

#The line below uses the print_model method to display the Model of our car
print(my_cars.print_model())

#The line below uses the print_make_and_year method to display the make and year of our car. We have to specify the arguments as we don't specify the make or year in the Method.
print(my_cars.print_make_and_year("F150", "2020"))