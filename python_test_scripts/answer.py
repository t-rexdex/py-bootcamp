# 1431. Kids with the greatest number of candies
def kidsWithCandies(candies: list, extraCandies: int) -> list:
    '''
    There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
    Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
    Note that multiple kids can have the greatest number of candies.

    '''
    bool_lst = [True if student + extraCandies >= max(candies) else False for student in candies]
    return bool_lst




# 121. Best time to buy and sell stock
def maxProfit(prices: list[int]) -> int:
    '''
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    '''
    for i in range(len(prices)):
        if prices[i] == min(prices):
            # remaining_days = lst[i+1:]
            max_profit = 0
            for day in prices[i+1:]:
                todays_profit = day - min(prices)
                if todays_profit > max_profit:
                    max_profit = todays_profit
                else:
                    profit = todays_profit
        elif min(prices) == prices[-1]:
            max_profit = 0
    return max_profit
        
