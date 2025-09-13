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
# "range"(5\) is built-in function will generate n numbers it expect integer value
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


cars = ["TATA", "ford", "BMW", "AUdi"]  # list of cars
for car in range(len(cars)):
    cars.append("Rolls Royece")
    cars.insert(3, "Lamborghini")
    print(cars)
    