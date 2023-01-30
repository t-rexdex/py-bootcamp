import sys
sys.path.append(r'./nile_project')

from nile import *
from main import * # not importing anything why did it lose access to the path
import pytest

# perhaps paramertize  the inputs to do multiple test with four sets of coords
# so that i do not have to keep inserting the same values all over the place

def test_get_distance():
    # answer expected to get from above inputs
    expected_ans = 0.45124

    ## coordinates for the test
    from_lat, from_long = (0,0)
    to_lat, to_long = (1,1)

    # use given inputs to receive answer
    received_ans = round(get_distance(from_lat, from_long, to_lat, to_long), 5) # rounding to   make sure answers match

    assert expected_ans == received_ans
    # need to add test with args that are not int/float should fail

    ## coordinates for the test
    from_lat, from_long = (0,0)
    to_lat, to_long = (1.0,1.0)

    # use given inputs to receive answer
    received_ans = round(get_distance(from_lat, from_long, to_lat, to_long), 5) # rounding to   make sure answers match

    assert expected_ans == received_ans

    ## test to throw an error if lat and lon values fall out of range
    from_lat, from_long = (-90,0)
    assert from_lat >= -90 and from_lat <= 90
    assert from_long >= -90 and from_long <= 90
    to_lat, to_long = (1,180)
    assert to_lat >= -180 and to_lat <= 180
    assert to_long >= -180 and to_long <= 180

    # need to do test with mismatch type error should fail

    
def test_format_price():
    """See if format_price can handle both integer and float"""
    price = 10
    answer = "$10.00"
    assert answer == format_price(price)

    price = 9.0
    answer = "$9.00"
    assert answer == format_price(price)

    # what other tests can you add to this? What else makes sense?



# should this be grouped with test_shipping?
def test_shipping_cost():

    expected_ans = '$1.04'
    ## coordinates for the test
    from_lat, from_long = (0,0)
    to_lat, to_long = (1,1)
    returned_ans = calculate_shipping_cost(from_lat, from_long, to_lat, to_long)
# the imported method broke and isnt reading from path
    assert expected_ans == returned_ans


driver1 = Driver(4, 10)
driver2 = Driver(7, 20)
def test_calulate_driver_cost():

    pass

def test_calculate_money_made():
    trip1 = Trip(200, driver1, 15)
    trip2 = Trip(300, driver2, 40)  
    expected_ans = 445 
    pass