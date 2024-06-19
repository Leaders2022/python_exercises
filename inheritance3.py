class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
    def print_name(self):
        print(f"My name is {self.first_name} {self.last_name}, and I'm {self.age} years old.")


class Student(Person):
        def __init__(self, first_name, last_name, age):  #I have inherited these attributes from the parent class
            super().__init__(first_name, last_name,age)   #super is an in-built function used to call the inherited attributes


my_person= Person("George", "Okubi", 99)
my_person.print_name()
my_person2= Person("John", "Doe", 101)
my_person2.print_name()
my_person3= Person("Jane", "Bill", 112)
my_person3.print_name()

