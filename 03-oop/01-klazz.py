class Base:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello {self.name}!")


b = Base("World")
print(hasattr(b, "name"))  # True
print(getattr(b, "name"))  # "World"
setattr(b, "name", "Python")
print(getattr(b, "name"))  # "Python"
__dict__ = getattr(b, "__dict__")
print(__dict__)  # {'name': 'Python'}
# direct access
print(b.__dict__)  # {'name': 'Python'}

