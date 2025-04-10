import math_utils

def main():
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /, **, %): ")

        operations = {
            '+': math_utils.add,
            '-': math_utils.subtract,
            '*': math_utils.multiply,
            '/': math_utils.divide,
            '**': math_utils.power,
            '%': math_utils.mod,
        }

        if operator in operations:
            result = operations[operator](x, y)
            print("Result:", result)
        else:
            print("Invalid operator")

    except ValueError:
        print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    main()

    print("\nTest cases from math_utils:")
    print(f"add(4, 2) = {math_utils.add(4, 2)}")
    print(f"subtract(4, 2) = {math_utils.subtract(4, 2)}")
    print(f"multiply(4, 2) = {math_utils.multiply(4, 2)}")
    print(f"divide(4, 0) = {math_utils.divide(4, 0)}")
    print(f"power(2, 3) = {math_utils.power(2, 3)}")
    print(f"mod(5, 2) = {math_utils.mod(5, 2)}")
