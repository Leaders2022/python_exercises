class Animal:

    def speak(self):
        print("Animal Speaking")
#The child class Dogchild inherits another child class Dog

class Dog(Animal):
    def bark(self):
        print("dog barking")
#The child class Dpgchild inherits another child class Dog
class DogChild(Dog):
    def eat(self):
        print("Eating meat")
d= DogChild()
d.bark()
d.speak()
d.eat()