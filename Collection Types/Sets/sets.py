# Python offers various collection types for different purposes.
# In this lesson, we'll explore sets, a collection type that is perfect for collecting unique data.
# Sets, unlike lists and tuples, are unordered collections. They are created with curly brackets { }.
# Sets are unordered and don't support indexing or slicing.

# guests = {"Mery", "Anna", "Jonathan"}
# print(guests)
# print(guests[0]) will output in error

# dishes = ["Salad", "BBQ", "Spaghetti"]
# guests = {"Mery", "Anna", "Jonathan"}
# print(dishes[0])
# print(guests[0]) will output in error

# Sets can't have duplicates, which is very helpful when developers need to ensure that each item in a collection is unique. For example, in social media apps, your friends list should not have duplicates.

friends = {"Anna", "Mery", "Mery", "Jonathan"}

print(friends)

# Sets are mutable, meaning you can add or remove items from them.
# Use the add() and remove() functions, each with a value as an argument, to add or remove it from a set.

guests = {"Mery", "Anna", "Jonathan"}

# adds robert 
guests.add('Robert')
# removes mery
guests.remove('Mery')

print(guests)

# The append() function works only with ordered collection types, like lists, and adds an item to the end of the collection. Sets are unordered, that's why you can't use it on them.

#The clear() function doesn't accept an argument and removes all the items from a set.

guests1 = {"Mery", "Anna", "Jonathan"}

guests1.clear()

print(guests1) # will output "set()"

# The union() function called returns a new set with all elements from both sets, omitting duplicates.

set1 = {'apple', 'banana'}
set2 = {'banana', 'cherry'}
combined_set = set1.union(set2) # c1.concat(c2) in JavaScript
print(combined_set)

# The difference() function returns a set containing elements that are only in the first set and not in the second.

set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'orange'}
unique = set1.difference(set2)
print(unique)