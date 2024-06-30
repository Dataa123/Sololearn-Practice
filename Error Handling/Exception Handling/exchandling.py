# Exceptions often arise from a variety of causes, including invalid input, out-of-bounds indices, incompatible type operations, and logical errors in the code. The good news is that exceptions are often predictable, allowing developers to anticipate and handle them effectively.

# The execution of code containing exceptions will stop when the first exception arises

# prices = [59, 95, 78, 24]
# print(prices[10]) # IndexError

# incorrect syntax: SyntaxError
# out-of-range index: IndexError
# variable is not defined: NameError

# prices = [250, 300, "240", 400]
# total = sum(prices) # TypeError
# print(total)

# The sum() function only works with iterables containing numerical data types (int or float)

# Exceptions can often be predictable. To handle them and prevent program failure, you can use a try/except statement.
# The try block holds code that might cause an exception. If an exception occurs, execution of the try block stops, and the except block is executed, allowing the program to continue running.
# Exception handling allows you to prevent program failure by processing potential exceptions in the way you need.

# When you specify only one type of exception to be handled, other types of exceptions will not be covered. If these other exceptions occur, the program execution will fail.

# For instance, the execution of this code will fail because the exception it throws is not handled.

colors = ['red', 'yellow', 'green']

# try:
#     # index error
#     print(colors[10])

#     # wrong exception
# except NameError:
#     print("Error")

# # will not be executed
# print("Happy shopping")

# You can have multiple except blocks to handle each possible exception specifically. As a best practice, it is recommended to output a definitive message for each type of handled exception.

try:
    print(colors[10])
except IndexError:
    print("Out of range")
except NameError:
    print("Variable is not defined")

print("Happy Shopping")

# You can choose not to specify the exception type, which allows handling of any exceptions that may occur. While this approach is easier, the downside is that the error messages may not be as clear and helpful.

# try:
#     print(colors[10])
# except:
#     print("Error")

# Exceptions are very helpful when your program interacts with user input. While you can't control what a user inputs, you can control your program's behavior when the input doesn't match the expected format. For instance, this program expects a numerical value as input and will throw an exception when the user inputs a non-numerical one.

# price = input()

# try:
#     price_value = int(price)
# except ValueError:
#     print("Please enter a number")


# 🌟 Use a try/except block to handle exceptions and prevent program failure

# 🌟 If an exception occurs in the try block, the except block will be executed

# 🌟 You can handle exceptions without specifying the exception type

# You can use the finally statement to perform an operation after the try/except block, no matter if an exception occurred or not.

prices = [559, 879, "N/A", 349]

try:
    print(sum(prices))
except TypeError:
    print("Check the prices")
finally:
    print("Need help? Contact us")

# The else statement can be used in conjunction with the try/except block and will execute only when no error occurs in the try block.

books = ['harry potter', 'dune', 'emma']

try:
    choice = books[1]
except IndexError:
    print("Out of range")
else:
    print(choice + " is a great choice!")
# output - dune is a great choice!

# products = ['ball', 'toy', 'paper']
# try:
#     count = len(products)
# except:
#     print("Error")
# else:
#     print("Count of products:", count)
# output - count of products: 3

# You can trigger your own exceptions based on specific conditions using the raise statement. This will immediately stop the program's execution and indicate an error has occurred.

print("Rate from 0 to 10")

rate = 15

if rate > 10 or rate < 0:
    raise ValueError

# To make the exceptions more helpful for the program users you can add a message describing the error.

rating = 15

if rating > 10 or rating < 0:
    raise ValueError("Rate from 0 to 10")

# 🌟 the finally keyword is used to execute code after a try/except block, regardless of whether an exception was raised

# 🌟 the else keyword, used with try/except, runs only if the try block is error-free

# 🌟 custom exceptions can be triggered using the raise keyword