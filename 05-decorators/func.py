# function first-class citizen
# can be passed as arguments

def hello():
    print("Hello")

greet = hello
print(greet)
print(greet())

####
print("#########")
def hello(func):
    func()

def greet():
    print("Still here")

a = hello(greet)
print(a)

#### Higher order function
# accepts function as argument
# returns function as result
def greet2():
    def func():
        return 5
    return func

print(greet2())