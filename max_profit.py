## Max Profit 
#
# Youre given an array of positive integers representing the prices of a single stock on various days (each index in the array
# reresents a different day). Youre also given an integer k, which represents the number of transactions you're allowed to make. 
# One transaction consists of buying the stock on a given day and selling it on another, later day. 
# 
# Write a function that returns the maximum profit that you can make by buying and selling the stoc, given k transactions. 
# 
# Note that you can only hold one share of the stock at a time; in other words, you cant buy more than one share on the stock
# on any given day, and you cant buy a share of the stock if youre still holding another share. Also you dont need to use all 
# k transactions that youre allowed.


# Sample input 
# prices = [5, 11, 3, 50, 60, 90] 
# k = 2 

# Expected output 
# 93  ## [Buy: 3, Sell: 11, Buy 3, sell: 90]


def maxProfitWithTransactions(prices, k):
    if not len(prices):
        return 0 
    profits = [[0 for d in prices] for t in range(k + 1)]

    for t in range(1, k + 1):
        maxThusFar = float("-inf")
        for d in range(1, len(prices)):
            maxThusFar = max(maxThusFar, profits[t - 1][d - 1] - prices[d - 1])
            profits[t][d] = max(profits[t][d - 1], maxThusFar + prices[d])
        return profits[-1][-1]


print(maxProfitWithTransactions([5, 11, 3, 50, 60, 90], 2))
