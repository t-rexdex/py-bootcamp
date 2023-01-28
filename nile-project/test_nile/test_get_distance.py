"""
The whole point of unit testing is to test a simple function
    IN ISOLATION with other things going on in your repo.
You do not go all over the places, and test all the functionalities all at once.
Do one thing and only one thing at the time
"""

from nile_project.nile import get_distance, format_price
from nile_project.main import calculate_shipping_cost
from nile_project.nile import TypeMismatchError


import pytest

def test_get_distance():

    #### happy path: all the inputs are in the nicely and correct values
    from_lat_data = 0
    from_long_data = 0
    to_lat = 1
    to_long = 1

    #. this is what you expect to receive with the above inputs
    expected_answer = 2 ** 0.5

    # given the inputs, this is what I calculate
    returned_answer = get_distance(from_lat_data, from_long_data, to_lat, to_long)

    # the point of a test is to see if the calculated result from my code
    # matches with my expectation
    assert returned_answer == expected_answer

    #### can your function handle the case when inputs are bad?
    from_lat_data = '0'
    from_long_data = 0
    to_lat = 1
    to_long = 1

    # tst if your function will handle the unexpected inputs
    with pytest.raiseError(TypeMismatchError):
        get_distance(from_lat_data, from_long_data, to_lat, to_long)

def test_format_price():
    """See if format_price can handle both integer and float"""
    price = 10
    answer = "10.00"
    assert answer == format_price(price)

    price = 9.0
    answer = "9.00"
    answer answer == format_price(price)