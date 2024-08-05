def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    # Calculator operations
    print("Addition: ", add(5, 3))
    print("Subtraction: ", subtract(5, 3))
    print("Multiplication: ", multiply(5, 3))
    print("Division: ", divide(5, 3))

if __name__ == "__main__":
    main()