a_int = 1
b_float = 1.0
c_complex = 1+1j
d_binary = 100010

print(f"Numbers int {a_int}, float {b_float} complex {c_complex}")
print(f"Type {type(a_int)}, {type(b_float)}, {type(c_complex)} ")

bin_a = bin(176) # 0b10110000 converts to string
print(f"Binary number {bin_a},{type(bin_a)}")
print(f"Back to decimal {int(bin_a, 2)}")

print(hash("ahoj"))

print(f"Binary {bin(10)}")
mask = 1 << 32
print(mask)
print(bin(mask))
print(10 & mask)
