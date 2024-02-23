
def calculator():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Error: Division by zero!")
            result = num1 / num2
        else:
            print("Invalid operator!")
            return

        print(f"{num1} {operator} {num2} = {result}")

    except ZeroDivisionError:
        print("Error: Division by zero! Please enter a non-zero denominator.")

    next_calculation = input("Let's do the next calculation? (yes/no): ")
    if next_calculation.lower() == "yes":
        calculator()
    else:
        print("Thank you!")

calculator()

