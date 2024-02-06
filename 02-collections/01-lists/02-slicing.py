L1 = [1, 2, 3, 4, 5]
# indexing
# first index
print(f"index 0 L1[0] {L1[0]}")
# last index
print(f"index -1 L1[-1] {L1[-1]}")
# second last index
print(f"index -2 L1[-2] {L1[-2]}")

# slicing
# [start:step:end]
print(f'slice L1[0:1] {L1[0:1]}')

# out of range
print(L1[2:7])
# first 2
print(L1[:2])
# from 2 to end
print(L1[2:])
# backwards
print(L1[-3:-1])
# 0 -> len(5)-1
print(L1[:-1])
print(L1[0:len(L1)-1])