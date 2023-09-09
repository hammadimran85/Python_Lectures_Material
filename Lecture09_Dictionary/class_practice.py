my_dict = {"name": "Alice", "age": 30, "city": "New York"}
name = my_dict["name"]  # Accessing the value associated with the "name" key
age = my_dict.get("age")  # Accessing the value associated with the "age" key
city = my_dict.get("city", "Unknown")  # Providing a default value if the key is not found

items = my_dict.items()  # Getting a list of key-value pairs
for key, value in items:
    print(f"Key: {key}, Value: {value}")

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 1, 'e': 2, 'f': 3}
dict3 = {'d': 4, 'e': 5, 'f': 6}
dict1.update(dict2)
print(dict1)
dict1.update(dict3)
print(dict1)

my_dict = {"a": 1, "b": 2, "c": 3}
removed_value = my_dict.pop("b")  # Removes the key "b" and returns its value
del my_dict["b"]  # Removes the key "b" and its associated value
print(my_dict)

print({**dict2,**dict3,**dict1})

import copy

dict1 = [[1, 2, 3], [4, 5, 6]]

deep_copy = copy.deepcopy(dict1)
shallow_copy = copy.copy(dict1)
print('Original Dict',dict1,id(dict1))
print('Deep Copy',deep_copy,id(deep_copy))
print('Shallow Copy',shallow_copy,id(shallow_copy))
shallow_copy[0][0] = 100
deep_copy[0][0] = 100
print()
print('Original Dict',dict1,id(dict1))
print('Deep Copy',deep_copy,id(deep_copy))
print('Shallow Copy',shallow_copy,id(shallow_copy))


