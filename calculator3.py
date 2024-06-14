def prompt_menu():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("""
Choose an operation from the list:
1. Addition
2. Subtraction
3. Multiplication
4. Exponentiation
5. Division
6. Division with remainder
    """)
    op = int(input("Enter the choice number: "))
    return a, b, op


def calculate():
    a, b, op = prompt_menu()
    if op == 1:
        print("Sum: {} + {} = {}".format(a, b, a + b))
    elif op == 2:
        print("Difference: {} - {} = {}".format(a, b, a - b))
    elif op == 3:
        print("Product: {} * {} = {}".format(a, b, a * b))
    elif op == 4:
        print("Power: {}^{} = {}".format(a, b, a ** b))
    elif op == 5:
        try:
            print("Quotient: {} / {} = {}".format(a, b, a / b))
        except:
            print("Division by 0 not possible!")
    elif op == 6:
        try:
            print("Division with remainder: {} / {} = {} Remainder: {}".format(a, b, a // b, a % b))
        except:
            print("Divsion by 0 not possible!")
    else:
        print("No such choice!")
    loop()


def loop():
    choice = input("Do you want to continue? (Y,N): ")
    if choice.upper() == "Y":
        calculate()
    elif choice.upper() == "N":
        print("Goodbye!")
    else:
        print("Invalid input!")
        loop()


calculate()
