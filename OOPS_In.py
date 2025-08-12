class Darshan:
    def __init__(
        self, My_name, My_age, My_address
    ):  # Constructor with parameters "__init__ is a special method in Python known as the constructor. It is automatically called when an object of a class is created.
        # Initialize instance variables
        self.My_name = My_name  # Name of the person instance variable Initialize instance variables with provided values
        self.My__age = My_age  #  Set the private age attribute with the provided value
        self.My_address = My_address  # Address of the person instance variable

        print("Name is:", self.My_name)
        print("Age is:", self.My__age)

    def show_details(self):
        """
                 Full Spoken Explanation (Script-Style):
        Here’s how you can explain this in front of your teacher:

        "In this program, I have created a class called Darshan with a constructor __init__ that initializes name, age, and address.
        Inside the constructor, I added print statements to show the name and age when the object is created.
        Then I defined a method show_details() that prints all the information of the object.
        I also added the __str__ method, which helps display the object in a readable string format when we use print(object).
        Finally, I created an object called person1, passed in the values, and called the show_details() method and print(person1) to display the object nicely
        """
        print("Full Details:")
        print("Name:", self.My_name)
        print("Age:", self.My__age) - +63
        print("Address:", self.My_address)

    def __str__(self):
        return f"{self.My_name}, {self.My__age} years old, lives at {self.My_address}"


# Create an object
person1 = Darshan("Darshan", 25, "Bengaluru")

# Show full details
person1.show_details()

# Print object using __str__
print(person1)
