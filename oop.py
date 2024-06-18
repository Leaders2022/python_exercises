class Student:
    #Constructor
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        #method
    def display(self):
        print(self.first_name, self.last_name)

        #object
my_student= Student(first_name= 'John', last_name= 'Smith')
my_student.display()
my_student2= Student(first_name= 'Eric', last_name= 'Were')
my_student2.display()
my_student3= Student(first_name='George', last_name='Okubi')
my_student3.display()
my_student4= Student(first_name='Doreen', last_name='Nyaga')
my_student4.display()
my_student5= Student(first_name='Leonel', last_name='Messi')
my_student5.display()


