# Methods of objects we've looked at so far are called by an instance of a class. However, there are other types methods that a class can have - class and static methods.

# Class methods are called on the class itself, not on individual instances. This allows their use without needing to create a class instance. They are especially useful for actions relevant to the class as a whole, rather than actions limited to a single object. Here's an example:

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def describe_book(self):
#         print(self.title, "by", self.author)

#     @classmethod
#     def books_in_series(cls, series_name, number_of_books):
#         print("There are", number_of_books, "books in the", series_name, "series")

# my_book = Book("Harry potter", "J.K Rowling")

# my_book.describe_book()

# Book.books_in_series("Harry Potter", 7)

# To call a class method you don't need to create an instance of the class. Instead, just use the class name, followed by a dot and the class method name.

# Instances share everything that a class has, including the class methods. This means that you call a class method on instances as well.

# my_book.books_in_series("Harry potter", 9)

# Static methods are similar to class methods, except they don't receive any additional arguments; they are identical to normal functions that belong to a class.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe_book(self):
        print(self.title, "by", self.author)

    @staticmethod
    def books_in_series(series_name, number_of_books):
        print("There are", number_of_books, "books in the", series_name, "series")

my_book = Book("Harry potter", "J.K Rowling")

my_book.describe_book()

Book.books_in_series("Harry Potter", 7)

# ( no cls )