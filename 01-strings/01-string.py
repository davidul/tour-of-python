'single quote string'
"double quote string"

print(type("Hello"))

m = '''
multi
line
string
'''
print(m)

# Concatenation
s1 = 'Hello'
s2 = 'World'

print(s1 + s2)

# conversion

print(str(100))

# Escape seq
print("Hi I'm David")
print('Hi I\'m David')
print("Hi I'm \"David\"")

# Formatting
name = 'Paul'
print(f'Hi {name}.')
print('Hi {}'.format('Paul'))
print('Hi {0} and {1}'.format('Paul', 'Chani'))
print('Hi {1} and {0}'.format('Paul', 'Chani'))
print('Hi {paul} and {another_name}'.format(paul='Paul', another_name='Chani'))

# Indexes
some = 'some'
print(some[0])
print(some[0:3])

# immutable
s1 = 'heloo'  # works
s1[0] = 'a'  # fail