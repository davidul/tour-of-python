# Python walkaround

## Installation
Virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

## Underscores

 - Single underscore `_` is used to indicate that a variable is temporary or insignificant.
 - Double underscore `__` is used to mangle class attributes.
 - Double underscore prefix and suffix `__var__` is used for special variables or methods (so-called “magic methods”).
 - Single underscore prefix `_var` is used to indicate that a variable or method is intended for internal use.
 - Single underscore suffix `var_` is sometimes used to avoid naming conflicts with Python keywords.

### Dunder methods
Control Object creation
- `__new__` - called before the object is created
- `__init__` - called after the object is created

`__new__` creates empty object and `__init__` initializes it.

Introspection
- `__dir__` - called when dir() is called on the object, print all attributes of the object

Attribute access
- `__getattr__` - called when an attribute is not found in the usual places
- `__setattr__` - called when an attribute is set
- `__delattr__` - called when an attribute is deleted
- `__getattribute__` - called when an attribute is accessed

## Walkaround

Fast walkaround of Python.

- variables
- loops
- conditions
- classes

## Collections

- list
- dictionary
- tuple
- set

### List
Use square brackets to create a list in Python.

Here are some common list methods in Python:

- append() - adds an element to the end of the list. Important: this method modifies the original list.
- extend() - extends the list with elements from another iterable object, such as a string or another list.
- insert() - inserts an element at a specific index in the list.
- pop() - removes and returns the last element in the list.
- remove() - removes the first occurrence of an element in the list.
- reverse() - reverses the order of elements in the list.
- sort() - sorts the elements in the list based on their natural ordering (for example, strings are sorted lexicographically).
- slice() - returns a new list containing a specified range of elements from the original list.

You can also use list comprehension to create a list with specific values or conditions. For example:

```python
my_list = [x**2 for x in range(1, 5)] # Output: [1, 4, 9]
```

### Dictionary
Here are some common dictionary methods in Python:

- get() - returns the value associated with a given key. If no such key is found, it raises a KeyError.
- setdefault(key, default) - sets the value of the specified key to the default value if it doesn't exist yet.
- popitem() - removes and returns an arbitrary (key, value) pair from the dictionary.
- items() - returns a list of all the key-value pairs in the dictionary.
- keys() - returns a list of all the keys in the dictionary.
- values() - returns a list of all the values in the dictionary.
- copy() - creates a new dictionary with the same mappings as the original dictionary, but with its own reference to the underlying data structure.
- update(other) - updates the dictionary with the key-value pairs from another dictionary or iterable object.

### Tuple

### Set