# Let's imagine you need to create a list containing numbers from 1 to 50.

# Here is the code you would need to write:

nums = []

for i in range(1, 51):
    nums.append(i)

print(nums) # output - **numbers from 1 to 50**

# List comprehensions are useful shorthands for such operations. They offer a shorter and more readable way to create lists with various settings using just a single line of code.

# List comprehensions are created using square brackets []

nums1 = [i for i in range(1,51)]

print(nums1) # output - **numbers from 1 to 50**

# Here is the generic syntax and structure of a list comprehension:

# 1. <variable>: the variable that will store the newly created list
# 2. <expression>: an expression performed on each item. If no specific action is needed, the item itself is used
# 3. <item>: the current item being processed
# 4. <iterable>: any iterable object, such as ranges, lists, strings, tuples, and sets

# Lists and Strings are iterable

# You can apply any expression to each item in the list being created with a list comprehension.

# For instance, the following code doubles each value in range(10) and stores the results in a list:

nums2 = [i * 2 for i in range(10)]

print(nums2) # output - [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# ------------------------------------------------------

nums3 = [i + 1 for i in range(10)]

print(nums3) # output - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# You can use a list as the iterable in a list comprehension.

# For example, this code will iterate through the original list of tags, adding a '#' symbol to the beginning of each tag to create a new list of hashtags.

tags = ["travel", "vacation", "journey"]

hashtags = ["#" + i for i in tags]

print(hashtags) # output - ['#travel', '#vacation', '#journey']

cities = ["madrid", "paris", "lisabon"]

cities_cap = [i.capitalize() for i in cities]

print(cities_cap) # output - ['Madrid', 'Paris', 'Lisabon']

# incoporate - ჩართვა

# You can incorporate a condition into a list comprehension, placed after the iterable.

# For example, the following code filters out names that start with B

users = ["Brandon", "Emma", "Brian", "Sophia", "Bella", "Ethan", "Ava", "Benjamin", "Mia", "Chloe"]

group1 = [i for i in users if i[0] == "B"]

print(group1) # output - ['Brandon', 'Brian', 'Bella', 'Benjamin']

names = ["Brandon", "Emma", "Brian", "Sophia", "Bella", "Ethan", "Ava", "Benjamin", "Mia", "Chloe"]

group2 = [i for i in names if i[0] != "A"]

print(group2) # output - ['Brandon', 'Emma', 'Brian', 'Sophia', 'Bella', 'Ethan', 'Benjamin', 'Mia', 'Chloe']

sports = ["Football", "Basketball", "Tennis", "Golf", "Volleyball"]

group3 = [i for i in sports if "ball" in i]

print(group3) # output - ['Football', 'Basketball', 'Volleyball']

scores = [68, 74, 89, 64, 85, 93]

high_scores = [i for i in scores if i > 80]

print(high_scores) # output - [89, 85, 93]

# 🌟 list comprehensions provide a concise and readable method for creating lists, allowing you to define various settings in just a single line of code

# 🌟 with list comprehensions, you can apply any expression to each item in the list being created

# 🌟 you can also incorporate a condition into a list comprehension

a, b = 5, 10