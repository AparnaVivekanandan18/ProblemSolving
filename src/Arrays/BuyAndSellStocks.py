# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of 
# the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.


# This is all about profit calculation of buying and selling
# I am here going to consider the inputs in python list
# [7,1,2,4,5,6]
# I am going to solve using Greedy technique - but the optimised way is to solve using "Memoisation technique"

def BuyAndSell(price_list) -> int:
    profit = 0
    len_price_list = len(price_list)
    for i in range(1,len_price_list):
        sell_price = price_list[i]
        buy_price = price_list[i-1]
        if buy_price < sell_price:
            profit = profit + (sell_price - buy_price)
    return profit


# Execution starts here
try:
    print("Enter the number of days, the stock is open for buying and selling")
    total_days = int(input())
    price_list = []
    print("Enter the prices")
    for i in range(total_days):
        price = int(input())
        price_list.append(price)
except ValueError as e:
    print("Invalid Input !")

max_profit = BuyAndSell(price_list)
if max_profit > 0:
    print("the maximum possible profit::", max_profit)
else:
    print("There is no way of getting profit")
