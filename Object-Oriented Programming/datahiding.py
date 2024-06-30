# Data hiding is a key idea in making code with objects (like in games or apps) safer and cleaner. It means keeping some parts of an object private so that only certain parts of your code can change them. This helps prevent mistakes and keeps your code easy to manage.

# In programming, sometimes it's crucial to 'protect' certain class attributes and methods from being accessed outside the class. This is called data hiding and ensures the integrity and security of the data, preventing unintended or harmful modifications.

# In Python, data hiding has two levels. The first involves prefixing an attribute with a single underscore _, signaling it's meant for internal use and should be viewed as 'protected'.

# class Car:
#     def __init__(self, model, year, odometer):
#         self.model = model
#         self.year = year
#         self._odometer = odometer
    
#     def describe_car(self):
#         print(self.year, self.model)

#     def read_odometer(self):
#         print("Odometer:", self._odometer, "miles")

# my_car = Car("Audi", 2020, 15000)

# my_car.describe_car()
# my_car.read_odometer()


# Attributes with a single underscore are accessible but considered protected by convention, signaling they're for internal use and should be accessed cautiously outside the class.

# The next level of data hiding involves making an attribute private. This is achieved by prefixing the attribute name with two underscores (e.g., __attribute). In this case, unlike protected attributes, this is not just a convention - it limits its access outside the class through name mangling, enhancing data protection and encapsulation. This method is used for sensitive or internal data, strongly discouraging external access.

class Car:
    def __init__(self, model, year, odometer):
        self.model = model
        self.year = year
        self.__odometer = odometer

    def describe_car(self):
        print(self.year, self.model)

    def read_odometer(self):
        print("Odometer:", self.__odometer, "miles")

my_car1 = Car("Audi", 2020, 15000)

my_car1.read_odometer()

# print(my_car1.__odometer) # (results in error)

# Accessing a private attribute directly from outside its class is generally discouraged in Python. However, Python employs name mangling for private attributes, which means you can access them using a specific naming convention from outside the class if necessary. 

print(my_car1._Car__odometer)

# Public: Attributes and methods that are accessible from anywhere.
# Protected: Attributes and methods that are accessible within the class itself and its subclasses.
# Private: Attributes and methods that are accessible only within the class itself.