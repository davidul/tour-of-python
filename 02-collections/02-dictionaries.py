# create new dictionary 
my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)
print(my_dict['key1'])

# key must be hashable
# value can be any type

# add new key-value pair
my_dict['key3'] = 'value3'

# update value of existing key
my_dict['key1'] = 'new value1'

# get method
print(my_dict.get('key1','default value'))
print(my_dict.get('key10','default value'))

# key and values
print(my_dict.keys())
print(my_dict.values())
# iterate over keys
print("Iterate over keys")
for key in my_dict.keys():
    print(key)

# delete key-value pair
print("Before", my_dict)
del my_dict['key1']
print("After", my_dict)

# items
print(my_dict.items())
items = my_dict.items()
print(type(items))
for key, value in items:
    print(key, value)


# in operator
print('key1' in my_dict)

# len
print(len(my_dict))

# pop
print(my_dict.pop('key2'))

# popitem
print(my_dict.popitem())

# clear
my_dict.clear()
print(my_dict)

