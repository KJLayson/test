def greet(name):
    return f"Hi there, {name}!"

def add(a, b, c=0):
    return a + b + c

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"

if __name__ == "__main__":
    print(greet("Bob"))
    print("Addition:", add(2, 3, 4))
    print("Division:", divide(6, 3))
