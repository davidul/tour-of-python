print("hello".lstrip("h"))  # "ello"
print("hello".rstrip("o"))  # "hell"
print("    hello".lstrip())  # "hello"
print("hello     ".rstrip())  # "helloß"

print("hello".strip("h"))  # "ello"
print("hello".strip("o"))  # "hell"

print("".zfill(5))  # "00000"

print("hELLO".capitalize())  # "Hello"