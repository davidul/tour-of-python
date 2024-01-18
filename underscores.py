class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myself(self):
        print(f'Hello my name is {self.name}')

def main():
    print("Hello world")
    s = "ahoj"
    dict(a=1, b=2, c=3)
    print(dir(s))
    p = MyClass("David", 45)
    p.myself()
    print(p.__class__)
    print(p.__class__.__name__)
    print(p.__dict__)
    print(p.__hash__())
    print(p.__getattribute__('name'))
    print(hasattr(p, 'name'))

if __name__ == '__main__':
    main()

