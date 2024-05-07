L1 = [1, 2, 3, 4, 5]
print(f'Original list {L1}')
# List Methods
# Length
print(f'len(L1) {len(L1)}')
# Append - modify list in place
L1.append(6)
print(f'After append(6) {L1}')
L1 += [7, 8, 9]
print(f'After +[7,8,9] {L1}')
L1.insert(3, 100)
print(f'insert(3,100) {L1}')
L1.extend([10, 100, 1000])
print(f' extend([10,100,1000]) {L1}')

### Remove
print("=== Remove ===")
# Removing
p = L1.pop() # default last
print(f'remove and retrieve last pop() {p}')
p = L1.pop(4)
print(f'remove and retrieve 4th pop(4) {p} {L1}')
L1.remove(1) # remove first occurence of value
print(f'remove first occurence of value L1.remove(1) {L1}')
L1.clear()
print(f'remove all clear() {L1}')
