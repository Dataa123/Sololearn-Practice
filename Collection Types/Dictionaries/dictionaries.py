# Key-value pairs are a fundamental concept in programming, allowing for efficient organization and retrieval of data.
# Dictionaries are collection types used to store data in key:value pairs, which are considered as items. They are ideal for organizing data into pairs, where each piece of data (value) has its unique identifier (key).

product = {
    "name": "Pen",
    "color": "Black",
    "price": 79
}

print(product.get("name")) # output - Pen

# While strings are the most commonly used data type for keys, other immutable types can also serve as keys. Values can be of any data type.

# Dictionaries can have duplicate values, but not duplicate keys.

# Values with duplicate keys will overwrite existing values.

car = {
    "brand": "Audi",
    "model": "Q5",
    "model": "A5",
    "year": 2008
}

print(car) # output - {'brand': 'Audi', 'model': 'A5', 'year': 2008}
print(car["brand"]) # output - Audi
print(car["model"]) # output - A5
print(car["year"]) # output - 2008


# Another way to access values in a dictionary is through the get() function.

# It's called on a dictionary using dot . notation and accepts the key as an argument

# You can get all the values and keys of a dictionary using the values() and keys() functions, respectively.
 
contact = {
    "name": "John",
    "company": "Google"
}

info_keys = contact.keys()
info_values = contact.values()

print(info_keys) # output - dict_keys(['name', 'company'])
print(info_values) # output - dict_values(['John', 'Google'])

# The items() function returns all the key:value pairs in a dictionary.

info_items = contact.items()

print(info_items) # output - dict_items([('name', 'John'), ('company', 'Google')])

# 🌟 Dictionaries are collection types used to store data in key:value pairs

# 🌟 Dictionaries can have duplicate values, but not duplicate keys

# 🌟 You can access a single value in a dictionary using the get() function

# 🌟 The values(), keys(), and items() functions are used to retrieve different collections of data from a dictionary

# --------------------------------------------------------------------------------------------------------

# Dictionaries are frequently used in modern applications, and proficiency in working with them is crucial for developers to write efficient code.

# You can use keys not only to access values in a dictionary, but also to change them.

user = {
    "name": "Data",
    "age": 16
}

user["age"] = 17

print(user["age"]) # output - 17
print(user.items()) # output - dict_items([('name', 'Data'), ('age', 17)])

# You can add a new item by providing a new key and assigning a value to it.

user["lastname"] = "Diasamidze"

print(user.items()) # output - dict_items([('name', 'Data'), ('age', 17), ('lastname', 'Diasamidze')])

# The update() function updates the dictionary with the items from the given argument.
# The argument for the update() function should be a dictionary, meaning it should start with { and end with }

user.update({"name": "Luka"})

print(user.items()) # output - dict_items([('name', 'Luka'), ('age', 17), ('lastname', 'Diasamidze')])

# The update() function can accept dictionaries with multiple items. If an item is new, it will be added to the original dictionary.

car_dict = {
    "brand": "BMW",
    "color": "Black"
}

car_dict.update({"color": "Red", "doors": 4})

print(car_dict.items()) # output - dict_items([('brand', 'BMW'), ('color', 'Red'), ('doors', 4)])

# The pop() function removes the item with the specified key name. It accepts the key of the item you want to remove as an argument.

car_dict.pop("doors")

print(car_dict.items()) # output - dict_items([('brand', 'BMW'), ('color', 'Red')])

# You can use the in operator to check if a key or a value occurs in a dictionary. (output is boolean)

print("brand" in car_dict) # output - True
print("doors" in car_dict) # output - False
# To check if a value occurs in a dictionary, you need to use the values() function.

print("Red" in car_dict.values()) # output - True
print("brand" in car_dict.keys()) # output - True

# You can iterate through a dictionary using a for loop.

# If you loop through a dictionary, it will return the keys.

car_dict1 = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Color": "red"
}

for i in car_dict1:
    print(i) # output - (line 1 - Brand) (line 2 - Model) (line 3 - Color)

# 1st way
for i in car_dict1:
    print(car_dict1[i]) # output (line 1 - Ford) (line 2 - Mustang) (line 3 - red)

# 2nd way
for i in car_dict1.values():
    print(i) # output (line 1 - Ford) (line 2 - Mustang) (line 3 - red)

# 🌟 Dictionaries are mutable

# 🌟 You can change or add dictionary items using the update() function

# 🌟 You can remove dictionary items with the pop() function

# 🌟 You can iterate through a dictionary using a for loop