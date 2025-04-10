def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero"

def power(x, y):
    return x ** y

def mod(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        return "Error: Divisionbyzero"

if __name__ == "__main__":
    print("Test cases for math_utils:")
    print(f"add(4, 2) = {add(4, 2)}")
    print(f"subtract(4, 2) = {subtract(4, 2)}")
    print(f"multiply(4, 2) = {multiply(4, 2)}")
    print(f"divide(4, 0) = {divide(4, 0)}")
    print(f"power(2, 3) = {power(2, 3)}")
    print(f"mod(5, 2) = {mod(5, 2)}")
