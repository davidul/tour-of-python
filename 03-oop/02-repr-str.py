class Represent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Represent(x={self.x}, y={self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'


r = Represent(1, 2)
print(r)
print(repr(r))
print(str(r))