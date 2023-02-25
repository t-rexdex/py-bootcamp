# 1431. Kids with the greatest number of candies
def kidsWithCandies(candies: list, extraCandies: int) -> list:
    bool_lst = [True if student + extraCandies >= max(candies) else False for student in candies]
    return bool_lst




