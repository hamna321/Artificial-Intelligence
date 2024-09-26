def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def modulus(x, y):
    return x % y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    
    
    choice = input("Enter choice (1/2/3/4/5): ")
    
    if choice in {'1', '2', '3', '4', '5'}:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        
        operations = {
            '1': add,
            '2': subtract,
            '3': multiply,
            '4': divide,
            '5': modulus
        }

        
        result = operations[choice](num1, num2)
        print(f"The result is: {result}")
    else:
        print("Invalid input")

# Call the calculator function
calculator()
