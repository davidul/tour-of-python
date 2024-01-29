# Decorator

def hello():
    print("Hello")

def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def greet():
    print("Still here")

greet()

# decorator syntax
# decorator with arguments
# multiple decorators

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        func(*args, **kwargs)
        print("After")
    return wrapper

@my_decorator
def greet2(name):
    print(f"Still here {name}")

greet2("David")