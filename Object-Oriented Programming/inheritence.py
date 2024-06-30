# The strength of OOP lies in organizing a program so its various components, treated as classes and objects, can interact smoothly.

# Inheritance is a key concept for situations where you have an existing class with defined attributes and behaviors, and you need a new class that not only shares these characteristics but also has its own unique ones. Inheritance allows the new class to 'inherit' properties from the existing class while adding or modifying specific features as needed.

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def move(self):
#         print("Moving")

# inheritence
# class Dog(Animal):
#     def bark(self):
#         print("Woof!")

# my_dog = Dog("Bob")

# inherited
# print(my_dog.name)
# my_dog.move()

# specific
# my_dog.bark()

# A class from which others are inherited is known as a superclass or parent class. Conversely, a class that inherits from another class is referred to as a subclass or child class.

# What if we want to not only inherit attributes but also add specific ones to a child class? In this case, we define an __init__ method in the child class. Use super().__init__() to inherit attributes from the parent class, and then define any additional attributes as usual.

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def move(self):
#         print("Moving")

# class Dog(Animal):
#     def __init__(self, name, breed, age):
#         super().__init__(name)
#         self.breed = breed
#         self.age = age
    
#     def bark(self):
#         print("Woof!")

# my_dog = Dog("Jax", "Bulldog", 5)

# # inherited
# print(my_dog.name)

# # additional
# print(my_dog.breed)
# print(my_dog.age)

# You can use the super()  function if you want to call a method from the parent class while overriding it.

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         print("making a sound")

# class Dog(Animal):
#     def __init__(self, name, breed, age):
#         super().__init__(name)
#         self.breed = breed
#         self.age = age

#     def sound(self):
#         super().sound()
#         print("Woof!")

# my_dog = Dog("Jax", "Bulldog", 5)

# my_dog.sound()


# Method overriding is a demonstration of another key concept in OOP - polymorphism. Polymorphism lets objects use methods in their own way, even if they share the same name.

# In this example, even though each animal in the animals list may be of a different subclass, the code can call sound() on each without needing to know its specific type.

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("making a sound")

class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name)
        self.breed = breed
        self.age = age

    def sound(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name)
        self.breed = breed
        self.age = age
    
    def sound(self):
        print("Meow!")


my_dog = Dog("Jax", "Bulldog", 5)
my_cat = Cat("Lily", "Ragdoll", 2)

animals = [my_dog, my_cat]

for animal in animals:
    animal.sound()