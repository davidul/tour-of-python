class Foo:
    def __init__(self):
        self.x = 42

    def bar(self):
        return "Hello, World!"


f = Foo()
print(f.__dir__())