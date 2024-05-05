class Attributes():
    def __init__(self):
        self.x = 42
        self.y = 43

    def __getattr__(self, name):
        return f"Attribute {name} not found"


a = Attributes()
print(hasattr(a, "x"))  # True
print(a.__getattribute__("x"))  # 42
print(getattr(a, "x"))  # 42
print(getattr(a, "z"))  # Not found
print(a.x)
#print(a["x"])