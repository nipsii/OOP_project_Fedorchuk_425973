# services/calculator.py

def validate_input(prompt, data_type=float):
    while True:
        try:
            return data_type(input(prompt))
        except ValueError:
            print("⚠️ Invalid input. Please try again.")

class Calculator:
    def calculate(self):
        num1 = validate_input("Enter first number: ")
        op = input("Enter operator (+, -, *, /): ")
        num2 = validate_input("Enter second number: ")

        try:
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2
            else:
                result = "Invalid operator"
        except ZeroDivisionError:
            result = "Error: Division by zero!"

        print(f"\n🧮 Result: {result}\n")