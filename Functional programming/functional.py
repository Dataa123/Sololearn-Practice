# def welcome(name):
#     return "Welcome, " + name

# def process_user(name, func):
#     return func(name)

# print(process_user("Alice", welcome))

# greet = lambda name: "Welcome, " + name

# print(greet("Data"))

# res = (lambda x, y: x + y)(10, 15)

# print(res)

# def mult(n):
#     return lambda a: a * n

# doubler = mult(2)(5)

# print(doubler)

# names = ["Alice", "Bob", "CHARLIE", "dEborah"]

# def capitalize(name):
#     return name.capitalize()

# capitalized = list(map(capitalize, names))

# print(capitalized)

# # The map function requires the first argument to be a function and the second argument to be an iterable.

# numbers = [1, 2, 3]

# doubled = list(map(lambda x: x * 2, numbers))

# print(doubled)

# products = {"Table": 110, "Sofa": 120, "Chair": 45, "Lamp": 70}

# filtered_products = dict(filter(lambda item: item[1] < 90, products.items()))

# print(filtered_products)

# def total(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result

# print(total(1, 2, 3, 4, 5))
# print(total(1, 2, 3, 4, 5, 6, 7))
# print(total(1, 2, 3))

# * - unpacking operator
# Note that args is just a name. You’re not required to use the name args. You can choose any name that you prefer.

# When defining a function with both regular arguments and *args, the regular arguments must come before *args in the function definition.

# def show_items(category, *items):
#     print("Category: " + category)
#     for item in items:
#         print(item)

# show_items("Electronics", "Laptop", "Smartphone", "Tablet")

# # The first line of the function definition, which includes the function name and its parameters, is called function signature.

# def display_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# display_info(name="Alice", age=30, city="New York")

# In a function definition, the order of arguments is important. First, regular arguments are listed, followed by *args for positional arguments, and finally **kwargs for keyword arguments.


# In Python, functions can be nested. This means you can define a function inside another function's body.

# def outer_function():
#     print("Hello from the outer function")

#     def inner_function():
#         print("Hello from the inner function")

#     inner_function()

# outer_function()

# You can also return the result of the nested function directly from within the body of the parent function.

# def greet(name):
#     print("Hey", name)

#     def account():
#         return "Your account is created!"
    
#     message = account()
#     return message

# print(greet("Bob"))

def order():
    def prepare():
      return "Your meal is being prepared!"
    status = prepare()
    return status

order()

# Imagine you have a function that generates a message. Your goal is to create another function that takes this original function as an argument and converts the original message into uppercase, without altering the original function's code.

# These functions are known as decorators. In the code below, the uppercase() function acts as a decorator, and the wrapper() function represents the modified (or decorated) version of the greet() function.

# def greet():
#     return "Welcome"

# def uppercase(func):
#     def wrapper():
#         orig_message = func()
#         modified_message = orig_message.upper()
#         return modified_message
#     return wrapper

# greet_upper = uppercase(greet)

# print(greet_upper())

# You can apply a decorator to a function using the @ sign. It improves the code readability and provides a clean separation between the function and its decoration.

def uppercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

@uppercase
def greet():
    return "Welcome!"

print(greet())