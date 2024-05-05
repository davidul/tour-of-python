class Base:
    def __init__(self, name):
        print("Initializing instance")
        self.name = name

    def __new__(cls, name):
        print("Creating instance")
        new_instance = super().__new__(cls)
        print(name)
        return new_instance

    def __repr__(self):
        return f"Base(name={self.name})"

    def __str__(self):
        return f"Base(name={self.name})"

    def __enter__(self):
        print("Entering context")
        return self

    def __format__(self, format_spec):
        return f"Base(name={self.name})"

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

#dunders
print(b.__class__)  # <class '__main__.Base'>
print(b.__class__.__name__)  # Base
print(b.__hash__())  # 876134534
print(b.__getattribute__("name"))  # Python
print(hasattr(b, "name"))  # True
print(hasattr(b, "age"))  # False
print(b.__dir__())
print(dir(b))
print(b.__repr__())
print(b.__str__())
print(b.__sizeof__())
print(b.__format__('Base'))



