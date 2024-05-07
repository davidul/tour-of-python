L1 = [1, 2, 3, 4, 5]
print(L1)
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
print(f'L1[2:7] {L1[2:7]}')
# first 2
print(f'first two L1[:2] {L1[:2]}')
# from 2 to end
print(f'from 2 to end L1[2:] {L1[2:]}')
# backwards
print(f'backwards L1[-3:-1] {L1[-3:-1]}')
# 0 -> len(5)-1
print(L1[:-1])
print(L1[0:len(L1)-1])