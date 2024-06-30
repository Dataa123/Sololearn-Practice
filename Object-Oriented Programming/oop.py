# In the real world, most things have a 'blueprint' and multiple instances of it. By 'blueprint,' we refer to an abstract set of properties and behaviors. Take, for example, a 'car.' It's a blueprint, or a general idea, covering properties like having four wheels, a color, engine power, and so on. The cars you see on the road are specific instances of this general blueprint, each with its unique characteristics like color, make, and model.

# To add attributes to a class, you must define the __init__ method. This method's first parameter is always self, which represents the instance of the class. Following self, you specify the attributes you wish to include. Then, inside the function, you assign values to the initialized object's attributes, setting their initial state.

# In addition to attributes, you can add custom behaviors to a class by defining functions within it. These functions, known as methods, should include the 'self' parameter to interact with the class instance. You can call these methods using the dot . notation, similar to how you access attributes.

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def honk(self):
        print("Beep beep!")

my_car = Car("Toyota", "Red")

my_car.honk()

# Everything in Python, including functions, is an object. For instance, integers are instances of the int class, and functions are instances of the function class, among others. This object-oriented nature underlies Python's flexibility and power.