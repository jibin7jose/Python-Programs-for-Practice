# Simple Calculator By Using Function.

# This Function Adds Two Numbers
def add(x, y):
    return x + y

# This Function Subtracts Two Numbers
def subtract(x, y):
    return x - y

# This Function Multiplies Two Numbers
def multiply(x, y):
    return x * y

# This Function Divides Two Numbers
def divide(x, y):
    return x / y

# This Function Modulus Two Numbers
def modulus(x, y):
    return x % y

print("Select Operation:-")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

while True:
    choice = input("Enter Choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", modulus(num1, num2))

        next_calculation = input("Let's Do Next Calculation...? (Yes/No): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
             