E = []
L1 = [1, 2, 3, 4, 5]
L2 = [1, 'a', True]

print(f"L1 array/list {L1}")

# indexing
print(f"index 0 L1[0] {L1[0]}")

# slicing
# [start:step:end]
print(f'slice L1[0:1] {L1[0:1]}')

# out of range
print(L1[2:7])
# 0 -> 2
print(L1[:2])
# 2 -> end
print(L1[2:])
# backwards
print(L1[-3:-1])
# 0 -> len(5)-1
print(L1[:-1])
print(L1[0:len(L1)-1])

# 2D (matrix)
m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# List Methods
len(L1)
# Adding
L1.append(6)
L1.insert(3, 100)
print(L1)
L1.extend([10,100,1000])
print(L1)

# Removing
p = L1.pop() # default last
print(p)
L1.pop(4)
print(L1)
L1.remove(1) # remove first occurence of value
print(L1)
L1.clear()
print(L1)

L1.extend([1,2,3,4,5])
# value, start, stop
i = L1.index(2) # returns first index of value
print(i)
print("Threes is in list:", 3 in L1)
print("Thirty is in list:", 30 in L1)

# count
print("=== Count ===")
L1.append(2)
print(f"There are {L1.count(2)} number of two")

# sort
print("=== Sorting ===")
L1.sort(reverse=True) # inplace sorting
print(L1)
L2 = sorted(L1) # returns sorted list
print(L1, '\n', L2)

# Copy
L3 = L1.copy()

# Reverse
L1.reverse()

# Range
print(list(range(1,10))) # 1-9
print(list(range(10)))   # 0-9

# unpacking
a,b,c = [1,2,3]
a,b,c, *d = [1,2,3,4,5]
print(d)
