# Best Time to Buy and Sell Stock


def max_profit_through_sliding_window(prices: list[int]) -> int:
    profit = 0
    buying = float("inf")

    for price in prices:
        if price < buying:
            buying = price
        elif price - buying > profit:
            profit = price - buying
        
    return profit



"""
def max_profit(prices: list[int]) -> int:
    most_profitable = 0

    for index, price in enumerate(prices):
        if index + 1 < len(prices):
            largest_local = max(prices[index + 1:])
            if (profit := price - largest_local) < most_profitable:
                most_profitable = profit
    return abs(most_profitable)
"""


inputs = ([7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1])

for i in inputs:
    print(i, "\t\t", max_profit_through_sliding_window(i))
