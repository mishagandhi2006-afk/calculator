# ==========================================
# Project: Simple Calculator with User History
# ==========================================

# List to store calculation history
history = []

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Function to display history
def show_history():
    if len(history) == 0:
        print("\nNo calculations yet.\n")
    else:
        print("\n===== Calculation History =====")
        for item in history:
            print(item)
        print("===============================\n")

# Main program
while True:
    print("\n====== SIMPLE CALCULATOR ======")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. View History")
    print("6. Clear History")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "5":
        show_history()
        continue

    elif choice == "6":
        history.clear()
        print("History cleared successfully.")
        continue

    elif choice == "7":
        print("Thank you for using the calculator.")
        break

    elif choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                expression = f"{num1} + {num2} = {result}"

            elif choice == "2":
                result = subtract(num1, num2)
                expression = f"{num1} - {num2} = {result}"

            elif choice == "3":
                result = multiply(num1, num2)
                expression = f"{num1} * {num2} = {result}"

            elif choice == "4":
                result = divide(num1, num2)
                expression = f"{num1} / {num2} = {result}"

            print("Result:", result)
            history.append(expression)

        except ValueError:
            print("Invalid input! Please enter numeric values.")

    else:
        print("Invalid choice! Please select between 1 and 7.")