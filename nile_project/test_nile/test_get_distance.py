from nile_project.main import * # not importing anything why did it lose access to the path
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
    # now to utilize Notreal_lat_or_long exception class to handle unreal input
    from_lat, from_long = (-91,0)
    to_lat, to_long = (1.0,1.0)

    with pytest.raiseError(Unreal_Lat_or_Long(from_lat, from_long, to_lat, to_long)):
        get_distance(from_lat, from_long, to_lat, to_long)
    ''' getting the following error message:
    name = 'raiseError'

    def __getattr__(name: str) -> object:
        if name == "Instance":
            # The import emits a deprecation warning.
            from _pytest.python import Instance
    
            return Instance
>       raise AttributeError(f"module {__name__} has no attribute {name}")
E       AttributeError: module pytest has no attribute raiseError

/usr/local/Caskroom/miniconda/base/envs/bootcamp/lib/python3.11/site-packages/pytest/__init__.py:169: AttributeError
    '''

    
def test_format_price():
    """See if format_price can handle both integer and float"""
    price = 10
    answer = "$10.00"
    assert answer == format_price(price)

    price = 9.0
    answer = "$9.00"
    assert answer == format_price(price)

    # what other tests can you add to this? What else makes sense?


def test_shipping_cost():
    expected_ans = '$1.04'
    # with shipping_type = 'Overnight' as the default
    ## coordinates for the test
    from_coords = (0,0)
    to_coords = (1,1)
    returned_ans = calculate_shipping_cost(from_coords, to_coords)
# the imported method broke and isnt reading from path
    assert expected_ans == returned_ans

