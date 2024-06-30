# Tuples, like lists, are ordered collections of items created with parentheses.
# The items in tuples also have their indexes, starting from 0. You can access the items in tuples just like you do with lists.
# So, what's the difference between tuples and lists? Tuples are immutable.
# They are useful when the data stored in collections shouldn't be accidentally modified during the program execution. For example, in a GPS navigation application, the coordinates of landmarks should remain constant

# my_tuple = (1, 2, 3, 4)
# my_tuple.append(5)

# print(my_tuple)

# error because tuples are immutable

my_string = "Data"

print(my_string.replace("D", "T"))

print(my_string)

# strings are immutable too. once the initial string is created, none of the function/methods that act on it change it directly, they simply return new strings.

scores = (7, 9, 9, 8, 9)
print("# of 7:",scores.count(7))

# You can use the count() function to calculate the number of occurrences of an item in a tuple.

# Many functions used with lists can also be used with tuples, as long as their purpose doesn't include modifying them.

# Count the number of items in the ids tuple using the len() function and store the result in the count variable

# The max() function returns the maximum value in a collection.

# You can use tuples in any control flow structures, such as if-else statements and loops, just as you would with lists.

# UNPACKING###############################################################
# While unpacking, the number of variables should match the number of items in the tuple. Otherwise, the program will result in an error.
birthday_date = (12, "August", 1993)
day, month, year = birthday_date

print(day)
print(month)
print(year)

# The * operator in tuple unpacking is used to gather multiple elements from the tuple into a list. This is useful when dealing with tuples of unknown length.

scores = (98, 96, 91, 88, 64)
winner, *rest = scores
print(winner)
print(rest)

# When unpacking a tuple, the variable prefixed with the * operator holds list