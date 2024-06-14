#a statement to check if someone is eligible to vote

age= int(input("Enter age :")) #this is inputoutput, not hardcoding.

if age >= 18:
    print("You are eligible to vote")
else:
    print("Sorry, you are under age") #You must indent the line

#Check if a number is odd or even
namba=int(input("Enter number :"))
if namba%5 == 0:
    print("Even")
else:
    print("Odd")