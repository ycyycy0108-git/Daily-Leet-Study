def maxProfit(prices):
    buypoint = 0
    sellpoint = 1
    max = 0
    while sellpoint < len(prices):
        cur = prices[sellpoint] - prices[buypoint]
        if prices[buypoint] > prices[sellpoint]:
            buypoint = sellpoint
        else:
            max = max(cur, max)
        sellpoint += 1
    return max



prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]


print(maxProfit(prices))