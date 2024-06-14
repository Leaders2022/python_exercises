a = 3
b =45.8
c = "emobilis"
d = True
e = False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

str= "Welcome to coding"
str2= "at emobilis Training Academy"

print(str[0:4])
print(str[5])   #Start counting from 0
print(str+str2)  #This is called concantination

fnames=["Erick", "Mercy", "Purie", "Joy", "Lenny"]  #List datatype
print(type(fnames))
print(f"My name is {fnames[0]}")
fnames[0]="Jane"
print(f"My name is {fnames[0]}") #use box brackets for datatypes
#list is mutable
matunda= ("Banana", "Mangoes", "Pineapples", "Oranges")  #Tuple datatype
print(f"I like eating {matunda[2]}")
#tuple is immutable
magari={"Vanguard", "Rav4", "Range Rover", "Mistubishi", "Nissan"} #set data structure
#sets do not have indices
#set is unordered
print(fnames)
print(matunda)
print(magari)

#Dictionary datatype. Use curly brackets
mydict = {"Age": 20, "Salary": 100000, "Gender": "Male", "name": "John", "Favmeal": "Bananas"}  #key value
print(type(mydict))
print(f"The age of the employee is {mydict['Age']}")
print(f"The salary of the employee is {mydict['Salary']}")
print(f"The employee is a {mydict['Gender']}")
print(f"And his name is {mydict['name']}")
print(f"And he likes eating {mydict['Favmeal']}")

