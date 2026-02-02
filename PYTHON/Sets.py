# #what is sets in python 
# #sets is a collection of unique elements 
# #sets is unordered and unindexed 
# #sets is mutable 
# #sets is unhashable 
# #sets is unordered 
# #sets is unindexed 
# #sets is mutable 
# #sets is unhashable 
# #sets is unordered 
# #sets is unindexed 
# #syntax:
# sets = {1, 2, 3, 4, 5}
# print(sets)
# print(type(sets))
# print(len(sets))
# print(max(sets))
# print(min(sets))
# print(sum(sets))
# print(sorted(sets))
# #print(reversed(sets)) #set' object is not reversible
# print(list(sets))
# print(tuple(sets))
# #print(dict(sets))
# print(set(sets))
# print(frozenset(sets))
# print(bool(sets))
# #print(complex(sets))
# #print(float(sets))
# #print(int(sets))
# print(str(sets))

# Initialize sets
python_course = set()
math_course = set()

def show_menu():
    print("\n===== Course Enrollment Menu =====")
    print("1. Add student to a course")
    print("2. List all students in a course")
    print("3. Find common students (Intersection)")
    print("4. Find all unique students (Union)")
    print("5. Find students in Python but not in Math (Difference)")
    print("6. Check if a student is enrolled")
    print("7. Remove a student from a course")
    print("8. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ").strip()
        course = input("Enter course (python/math): ").lower()
        if course == 'python':
            python_course.add(name)
        elif course == 'math':
            math_course.add(name)
        else:
            print("Invalid course name.")

    elif choice == '2':
        course = input("Which course? (python/math): ").lower()
        if course == 'python':
            print("Python Course Students:", python_course)
        elif course == 'math':
            print("Math Course Students:", math_course)
        else:
            print("Invalid course name.")

    elif choice == '3':
        common = python_course & math_course
        print("Students in both courses:", common)

    elif choice == '4':
        all_students = python_course | math_course
        print("All unique students:", all_students)

    elif choice == '5':
        only_python = python_course - math_course
        print("Python-only students:", only_python)

    elif choice == '6':
        name = input("Enter student name: ").strip()
        if name in python_course or name in math_course:
            print(f"{name} is enrolled in at least one course.")
        else:
            print(f"{name} is not enrolled.")

    elif choice == '7':
        name = input("Enter student name: ").strip()
        course = input("From which course? (python/math): ").lower()
        if course == 'python':
            python_course.discard(name)
        elif course == 'math':
            math_course.discard(name)
        else:
            print("Invalid course name.")

    elif choice == '8':
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
