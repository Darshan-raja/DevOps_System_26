# Function example

Declaration and definition
# def get_sum(number1, number2):     #declaration of the function
#     """Returns the sum of two numbers."""   #definition of the function
#     return number1 + number2  #returning the sum of the two numbers

# # Calling the function
# result = get_sum(456 ,56464)
# print("The sum is", result)

# def get_sum(number1, number2): #declaration of the function
#      sum = number1 + number2 #definition of the function
#      return sum;

# #calling the function
# get = get_sum(5665, 646546)
# print("the sum is", get)
#print("custom sum:", get_sum(654,546))

#ef get_sum(*Number):
# def get_sum(**kwargs): #kwargs,*Number is a keyword argument
#      return sum(kwargs.values())
#           # Calling the function with multiple arguments
# print("Sum from keyword args:", get_sum(a=5, b=5, c=20))git stash push --keep-index


#E-Commerce example using Functions
def E_commerce(cart_item, tax):
     total_item = sum(cart_item)
     tax_price = total_item * tax
     total_amount = total_item +tax_price
     return total_amount

cart_items = [20, 30, 40,]
print("Total amount after tax:", E_commerce(cart_items, 0.05))

#without functions agruments


def fn ():
     #without argruments
     return fn
returned = fn()
returned()

