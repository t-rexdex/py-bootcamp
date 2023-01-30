
import sys
sys.path.append("/Users/RexLAP/PycharmProjects/py_bootcamp/test_nile")

from nile import *
from main import * # not importing anything why did it lose access to the path
import pytest


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

    ## test to throw an error if lat and lon values fall out of the following ranges: [-90,90] and [-180, 180]
    # maybe add try and except?
    from_lat, from_long = (-9,0)
    assert from_lat >= -90 and from_lat <= 90
    assert from_long >= -90 and from_long <= 90

    to_lat, to_long = (1,180)
    assert to_lat >= -180 and to_lat <= 180
    assert to_long >= -180 and to_long <= 180

    # need to do test with mismatch type error should fail
    # holding off because i do not want to copy huy's code without understanding

    
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
    from_coords = (0,0)
    to_coords = (1,1)
    returned_ans = calculate_shipping_cost(from_coords, to_coords)
# the imported method broke and isnt reading from path
    assert expected_ans == returned_ans

expected_distance = 0.45124
driver_test = Driver(4, 10) # imports with no problems
def test_get_driver_time():
    expected_ans = 0.11281
    received_ans = expected_distance / driver_test.speed
    assert expected_ans  == received_ans
    # need to reuse driver_test.speed I probably should make a class to condense all of this 
    # for now i will do it the slow person way
def test_get_driver_price():
    expected_ans =1.1281
    driver_time_test = 0.11281
    driver_price_test = driver_test.salary * driver_time_test
    assert expected_ans == round(driver_price_test,4)

def test_calulate_smaller_driver_cost():
    # i know is a better way to call this stuff for the test
    driver2_test = Driver(7, 20)
    expected_ans = driver_test
    returned_price, returned_driver = calculate_smaller_driver_cost(expected_distance, driver_test, driver2_test)
    assert expected_ans == returned_driver

    # checking cheapest_price just to make sure
    expected_ans = 1.1281
    assert expected_ans == round(returned_price, 4)

def test_calculate_money_made():
    # trip1 = Trip(200, driver1, 15)
    # trip2 = Trip(300, driver2, 40)  
    # expected_ans = 445 
    pass

#  
