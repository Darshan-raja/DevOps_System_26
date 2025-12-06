# what is Recurusion?
# Recursion is a programming technique where a function calls itself in order to solve a problem.
# It is often used to solve problems that can be broken down into smaller, similar subpro

# def mummy():
#     print(" hey you are in mummy function")
#     return mummy()


# mummy()# stack overflow error in python is smart enough to detect it and stop the program after 996 timea


# def imyour(count):
#     if count >= 7:  # which is base case condition is used to stop the recursion
#         return
#     print("hey im your boyfriend")
#     imyour(count + 1)


# if __name__ == "__main__":
#     imyour(1)


def sort(arr, arr2):  # arr arr2 are parameters
    # arr = index

    if arr2[arr] > arr2[arr + 1]:  # comparing current element with next element arr2[arr is current element] > arr2[arr + 1] is next element and checking if current element is greater than next element  +1 is used to move to next element
        return False

    if arr + 1 == len(arr2) - 1:  # base case arr + 1 is equal to length of arr2 -1 means we have reached the end of the array +1 is used to move to next element -1 is used to move to previous element
        return True

    return sort(arr + 1, arr2)
# whole code is checking if the array is sorted or not using recursion

arr2 = [1, 2, 3, 9, 4]
print(sort(0, arr2))
