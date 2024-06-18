# CREATE A CLASS CALLED CARS WITH THE FOLLOWING ATTRIBUTES
# MODEL, YEAR OF MANUFACTURE, TYPE, COLOR
#
# CREATE A METHOD TO PRINT
# "MY DREAM CAR IS..... MANUFACTURED IN......BEING A......TYPE.......IN COLOR"
#
# INITIALISE WITH AT LEAST 5 OBJECTS

class Cars:
    #constructor
   def __init__(self, model, year_of_manufacture, type, color):
       self.model= model
       self.year_of_manufacture= year_of_manufacture
       self.type= type
       self.color= color

    #method
   def display(self):
        print(f"My dream car is {self.model}, manufactured in {self.year_of_manufacture} being {self.type}, {self.color} in color")

        #objects
my_cars= Cars(model="Toyota", year_of_manufacture="2020", type="Vanguard", color="Black")
my_cars.display()



