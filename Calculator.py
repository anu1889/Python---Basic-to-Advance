def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def divide(x,y):
    if y == 0:
        return "Error! Divison by Zero."
    else:
        return x / y

def mul(x,y):
    return x * y

def user_choice():
    print("Select Operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Muliply")
    print("5. Exit")
    return int(input("Enter Choice (1/2/3/4/5): "))

def basic_calc():
    while True:
        choice = user_choice()

        
        if choice == 5:
            print("Bye ;)")
            break

        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", sub(num1, num2))
        elif choice == 3:
            print("Result:", divide(num1, num2))
        elif choice == 4:
            print("Result:", mul(num1, num2))
        else:
            print("Invalid Input")

basic_calc()
