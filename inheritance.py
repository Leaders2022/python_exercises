class Animal:

    def __init__(self, type, color):
        self.type= type
        self.color= color

    def display(self):
        print(f"The fiercest animal is the {self.type} and is {self.color} in color")
my_animal= Animal("Lion", "brown")
my_animal.display()
my_animal= Animal("Elephant", "grey")
my_animal.display()
my_animal= Animal("Leopard", "brown")
my_animal.display()