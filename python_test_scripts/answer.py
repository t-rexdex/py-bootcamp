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
    # length = len(prices)
    # idx = 0
    # for day in prices:
    #     idx += 1
    #     for next_day in prices(idx+1:)
    # for day in prices:
    #     old_profit = 0
    #     if day == prices[0]:
    #         min = day
    #     elif day < min:
    #         min = day
    #     elif day > min and (day - min) > old_profit :
    #         profit = day - min
    #     elif day == min:
    #         pass
    #     else:
    #         profit = 0
    # print(profit)
    pass
# maxProfit([7,1,5,3,6,4])
# maxProfit([7,6,4,3,1])
lst = [7,5,3,6,4, 1]
length = len(lst)
idx = 3

for i in range(len(lst)):
    #go through each day
    if lst[i]  ==  min(lst):
        old_profit = 0
        for day in lst[i+1:]:
            profit = day - min(lst)
            old_profit = profit # the current train of thought has me wanting to go back and forth on nested if and for loops.
            #not good 
            print(f'Todays cost is {day}, and the profit to sell today would be {day-min(lst)}, and yesterdays profit was{ old_profit}')