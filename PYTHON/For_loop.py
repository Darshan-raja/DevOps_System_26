# what is loop?
# loop is a way to repeat a block of code multiple times
# type of loop
# 1. For loop
# 2. While loop
# 3. Nested loop

# <For loop>
# syntax: for in iterable:
#        statement
# Example of for loop
# for i in range(5):
#     print(i)
# i will take value from 0 to 4
#  is is a variable
# "range"(5) is built-in function will generate n numbers it expect integer value
# range(start, stop, step)
# for{vaiable name} in {iterable} in {collection}:
# {collection} is a list, tuple, set, dictionary, string
# {iterable} is a sequence of elements that can be iterated over
# for dg in range(8,10):
#       print(dg)


# print(value.count(4))

# for d in range(10, 5, 10):
# range(start, stop, step)
# start = 10: The first number in the sequence.
# stop = 5: The sequence stops before this number.
# step = 10 increment by 10 each time.
# The loop will only run once for the value 10.
#     print(d)
# for er in range(11, 11, -2):
#     # 0 start value
#     # 10 stop value
#     # 2 step value increment by 2
#     print(er)


# cars = ["TATA", "ford", "BMW", "AUdi"]  # list of cars
# for car in range(len(cars)):
#     # append method add element at the end os the list
#     cars.append("Rolls Royece")
#     cars.insert(1, "Lamborghini")  # (index, value)
#     print(cars)
# 3*1 = 3

# This code snippet is generating multiplication tables for numbers from 5 to 10.
# for i in range(5, 11):
#     print(f"Multiplication table of {i} is:")
# for j in range(1, 11):
#     # f meaning formatted string which is used to print variable value inside string
#     print(f"{i} * {j}= {i*j} ")
#


# how to implement for loop in python and real life project

# for loop with conditions to find even numbers in a list
# num = [23, 74, 34, 89, 94, 92]
# for i in num:
#     if i % 2 == 0:
#         print(f"{i} is even number")

# for num in range(4):
#     if num == 4:
#         # break  # use to exit the loop
#         continue
#     print(num)
# def imyour(count):
#     if count >= 7:
#         return
#     print("hey im your boyfriend")
#     imyour(count + 1)


# if __name__ == "__main__":
#     imyour(1)

# num = int(input("Enter a number : "))
# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()
# This code snippet is creating a pattern of asterisks in a grid format. It is using nested for loops to print asterisks in rows and columns. The outer loop `for i in range(1, 4):` controls the rows, and the inner loop `for j in range(1, 4):` controls the columns.
# for i in range(1, 4):
#     for j in range(1, 4):
#         # The end=" " parameter in the print function is used to add a space after each asterisk instead of moving to a new line.
#         print("*", end=" ")
#     # This print() is used to move to the next line after printing each row of asterisks.
#     print()


row = 5
for i in range(1, row+5):
    for k in range(1, row+1):
        print("*", end=" ")
    print()
