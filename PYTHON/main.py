# what is Recurusion?
# Recursion is a programming technique where a function calls itself in order to solve a problem.
# It is often used to solve problems that can be broken down into smaller, similar subpro

# def mummy():
#     print(" hey you are in mummy function")
#     return mummy()


# mummy()# stack overflow error in python is smart enough to detect it and stop the program after 996 timea


def imyour(count):
    if count >= 7:  # which is base case condition is used to stop the recursion
        return
    print("hey im your boyfriend")
    imyour(count + 1)


if __name__ == "__main__":
    imyour(1)
