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
# 93  ## [Buy: 5, Sell: 11, Buy 3, sell: 90]


def maxProfitWithTransactions(prices, k):
    profit = None 
    transaction = None

    if not len(prices):
        return 0   
    
    for i in range(0, len(prices)):
        eval = prices[i]

        for j in range(0, len(prices)):
            if i != j:
                if i < j:
                    transaction = prices[j] - eval
                if i > j:
                    transaction = eval - prices[j]
                if not profit:
                    profit = transaction
                if profit:
                    if profit < transaction:
                        profit += transaction 
    print(profit)
    return profit

maxProfitWithTransactions([5, 11, 3, 50, 60, 90], 2)
