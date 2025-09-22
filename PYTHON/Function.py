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
# print("custom sum:", get_sum(654,546))

# ef get_sum(*Number):
# def get_sum(**kwargs): #kwargs,*Number is a keyword argument
#      return sum(kwargs.values())
#           # Calling the function with multiple arguments
# print("Sum from keyword args:", get_sum(a=5, b=5, c=20))git stash push --keep-index


# E-Commerce example using Functions
def E_commerce(cart_item, tax):
    total_item = sum(cart_item)
    tax_price = total_item * tax
    total_amount = total_item + tax_price
    return total_amount


cart_items = [20, 30, 40,]
print("Total amount after tax:", E_commerce(cart_items, 0.05))

# without functions agruments


def fn():
    # without argruments
    return fn


returned = fn()
returned()


r = 4
f = 8
print(r // f, r % f)


def bot(prices: list[int]) -> None:
    profit = 0
    holding = False
    buy_price = 0

    print("Starting Trading Bot...\n")

    for i in range(1, len(prices)):
        yesterday = prices[i - 1]
        today = prices[i]

        # Buy signal: today's price > yesterday's
        if today > yesterday and not holding:
            buy_price = yesterday
            holding = True
            print(f"BUY on Day {i-1} at ${buy_price}")

        # Sell signal: holding and price is going to drop or end of list
        if holding and (today < yesterday or i == len(prices) - 1):
            sell_price = prices[i - 1]
            transaction_profit = sell_price - buy_price
            profit += transaction_profit
            holding = False
            print(
                f"SELL on Day {i-1} at ${sell_price} (Profit: ${transaction_profit})")

    print("\nTrading Complete.")
    print(f"Total Profit: ${profit}")
