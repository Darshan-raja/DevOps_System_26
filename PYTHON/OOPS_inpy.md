<what is oops in programming>
oop stands for object-oriented programming. it is a programming paradigm that revolves around the concept of objects and classes. in oops, data and behavior are encapsulated within objects, allowing for modular and reusable code. key principles of oops include:
1. <Classes>: a blueprint for creating objects, defining their properties and methods.
1(a). <Object>: an instance of a class, representing a specific entity with its own properties and behavior.
2. <encapsulation or bulding syntax:> bundling data and methods that operate on that data within a single unit (class).
3. <inheritance>: creating new classes based on existing ones
, allowing for code reuse.
4. <polymorphism>: enabling objects to be treated as instances of their parent class, allowing for flexibility in code.
5. <abstraction>: hiding complex implementation details and exposing only necessary features.
for example, consider a student to mention the Obejct

class student :
<Objects>
(varibale name or intance variable calling ) student.new = new student()  (<NEW> is keyword" class name student () is called Object 
with help of new keyword we can create new object in RAM of class student)
RAM segment Dynamic memory allcoation to the object
- When you create an object, Python allocates memory for it in the heap segment of RAM.
- This is called dynamic memory allocation.
- Each object gets its own space in memory to store its attributes (data) and methods (functions).
<Garbage collector> - Python automatically manages memory allocation and deallocation through a process called garbage collection.
<Constructor> - A constructor is a special method in a class that is automatically called when an object is created. it is used to initialize the object's attributes. Python constructors do not have a return type, not even None.

The <__init__> method is used to initialize a new object of the class.
It sets up the initial values for the object’s attributes when the object is created.
he <self> keyword refers to the current instance of the class.
It is used to access or store attributes and methods that belong to that specific object.
 Why is self necessary?
<It allows each object to store its own values.>
Without self, you can't assign or access instance-specific data.

<Access Modifiers>
- Public: accessible from anywhere
- Private: accessible only within the class
- Protected: accessible within the class and its subclasses

Encapsulation
- Encapsulation is a principle of object-oriented programming that involves bundling data and methods that operate on that data within a single unit (class).
- This allows for modular and reusable code, as well as better control over access to the data and methods.