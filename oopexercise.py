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
my_cars= Cars("Toyota", "2020", "Vanguard", "Black")
my_cars.display()
my_cars2=Cars("Toyota", "2023", "Rav4","White")
my_cars2.display()
my_cars3= Cars("Mercedes", "2019", "Benz E Class", "grey")
my_cars3.display()
my_cars4= Cars("Toyota",  "2018", "Land Cruiser", "black")
my_cars4.display()
my_cars5= Cars("Toyota", "2021", "Prado", "black")
my_cars5.display()
my_cars6= Cars("Toyota", "2023", "Landrover", "black")
my_cars6.display()


