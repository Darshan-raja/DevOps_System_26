# class Darshan:
#     def __init__(
#         self, My_name, My_age, My_address
#     ):  # Constructor with parameters "__init__ is a special method in Python known as the constructor. It is automatically called when an object of a class is created.
#         # Initialize instance variables
#         self.My_name = My_name  # Name of the person instance variable Initialize instance variables with provided values
#         self.My__age = My_age  #  Set the private age attribute with the provided value
#         self.My_address = My_address  # Address of the person instance variable

#         print("Name is:", self.My_name)
#         print("Age is:", self.My__age)

#     def show_details(self):
#         """Full Spoken Explanation (Script-Style):
#         Here’s how you can explain this in front of your teacher:

#         "In this program, I have created a class called Darshan with a constructor __init__ that initializes name, age, and address.
#         Inside the constructor, I added print statements to show the name and age when the object is created.
#         Then I defined a method show_details() that prints all the information of the object.
#         I also added the __str__ method, which helps display the object in a readable string format when we use print(object).
#         Finally, I created an object called person1, passed in the values, and called the show_details() method and print(person1) to display the object nicely
#         """
#         print("Full Details:")
#         print("Name:", self.My_name)
#         print("Age:", self.My__age)
#         print("Address:", self.My_address)

#     def __str__(self):
#         return f"{self.My_name}, {self.My__age} years old, lives at {self.My_address}"


# # Create an object
# person1 = Darshan("Darshan", 25, "Bengaluru")

# # Show full details
# person1.show_details()

# # Print object using __str__
# print(person1)


# class Book:
#     def __init__(self, title, book_name, author_name, price, year_of_publication):
#         # Intializing instance variable or attirbutes
#         self.title = title
#         self.book_name = book_name
#         self.author_name = author_name
#         self.price = price
#         self.__year_of_publication = year_of_publication  # Private attribute that cannot be accessed directly outside the class
#         self.__discount_percentage = (
#             0  # Private attribute that cannot be accessed directly outside the class
#         )

#     def borrow(self):
#         if self.is_available:
#             self.is_available: False
#             print(f"{self.title}has been borrowed.")
#         else:
#             print("The book is not available.")

#                def return_book(self):
#             self.is_avialable = True
#             print(f"{self.title}has been returned.")

#             self.is_available = True


#             book1 = Book("Python", "Python Programming", "Darshan", 500, 2011)
#             book1.borrow()
#             book1.show_boolk()
class Book:
    def __init__(self, title, book_name, author_name, price, year_of_publication):
        self.title = title
        self.book_name = book_name
        self.author_name = author_name
        self.price = price
        self.__year_of_publication = year_of_publication
        self.__discount_percentage = 0
        self.is_available = True  # Correctly initialized

    def borrow(self):
        if self.is_available:
            self.is_available = False  # Correct assignment
            print(f"{self.title} has been borrowed.")  # Fixed spacing
        else:
            print("The book is not available.")

    def return_book(self):
        self.is_available = True  # Fixed spelling
        print(f"{self.title} has been returned.")  # Fixed spacing

    def show_book(self):
        print(f"Title: {self.title}")
        print(f"Book Name: {self.book_name}")
        print(f"Author: {self.author_name}")
        print(f"Price: {self.price}")
        print(f"Available: {self.is_available}")


# ✅ Object creation and function calls — placed outside the class
book1 = Book("Python", "Python Programming", "Darshan", 500, 2011)
book1.borrow()
book1.show_book()
book1.return_book()
book1.show_book()


#         if self.__year_of_publicaton < 2011:
#             self.__discount_percentage = 10
#         else:
#             self.__discount_percentage = 0

#         print("You have borrowed the book")

#     def return_book(self):
#         print("You have returned the book")

#     def show_details(self):
#         print("Book Title:", self.title)
#         print("Book Name:", self.book_name)
#         print("Author Name:", self.author_name)
#         print("Price:", self.price)
#         print("Year of Publication:", self.__year_of_publicaton)
#         print("Discount Percentage:", self.__discount_percentage, "%")


# book1 = book("Python", "Python Programming", "Darshan", 500, 2011)
# book1.borrow()
# book1.show_details()

# book1.return_book()
