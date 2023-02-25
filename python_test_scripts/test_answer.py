from answer import kidsWithCandies, maxProfit
import pytest

@pytest.mark.parametrize('candies, extraCandies, expectedAns',[
        ([2, 3, 5, 1, 3], 3, [True,True,True,False,True]),
        ([4, 2, 1, 1, 2], 1, [True,False,False,False,False]),
        ([12, 1, 12], 10, [True,False,True])
    ])
def test_kids_wCandies(candies, extraCandies, expectedAns):
    assert  kidsWithCandies(candies=candies, extraCandies=extraCandies) == expectedAns


@pytest.mark.parametrize('prices, expectedAns', [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0) 
    ])
def test_maxProfit(prices, expectedAns):
    pass