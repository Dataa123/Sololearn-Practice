# In programming, bugs and errors are common, regardless of experience level. They can range from minor typos to complex logical errors. 

# The computer reads and executes instructions line by line, from top to bottom. The execution of the program will be interrupted at the first error encountered.

# Mistakes in Python can be broadly categorized into two types: bugs and exceptions

# Bugs are flaws or mistakes in a program's code, leading to incorrect or unintended behavior. This doesn't necessarily stop the program from running to completion, but it can result in wrong outputs or behaviors.

# Bugs, often caused by logical errors, can lead to unexpected or incorrect results. For example, the code below is meant to concatenate name and surname with a space. It executes without error but omits the space, which indicates a bug.

name = "Mery"
surname = "Osborn"
print(name + " " + surname)

#The code above is designed to create a list of capitalized names. While it executes successfully, it results in incorrect output. Find the bug:

data = ["anna", "bob", "mery"]
names = [x.upper() for x in data]

print(names)

# upper() should be capitalize()

# Exceptions are another category of mistakes in programming. These are specific errors that occur during a program's execution and interrupt its normal flow when first encountered.

# There are several types of exceptions in Python.

# The NameError exception is raised when an unknown variable is used.
# The SyntaxError exception is raised when a syntax mistake in the code is encountered. This could be due to various reasons such as missing punctuation (like commas, parentheses or colons).
# The IndexError is raised when you attempt to access an element of an iterable, ordered collection, such as lists and tuples, using an index that is outside its valid range.
# The TypeError exception is raised when a function is called on a value of an inappropriate type. For example, the len() function can be called only on iterables (like strings, lists, etc.). for example: len(True), len(5)
# The ValueError exception is raised when a function receives a value of the correct type, but the value itself is inappropriate or unacceptable.
# For example, the int() function can be called on strings, but only when all characters in the string are numerical values.

# 🌟 Bugs are mistakes that may not interrupt execution but can cause incorrect behavior

# 🌟 Exceptions are errors that occur during execution and disrupt the program's flow

# 🌟 There are various types of exceptions