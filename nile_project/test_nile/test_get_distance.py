from nile_project.nile import get_distance, format_price
import pytest

def test_get_distance():
    # answer expected to get from above inputs
    expected_ans = 0.45123

    # coordinates for the test
    from_lat, from_long = (0,0)
    to_lat, to_long = (1,1)

    # use given inputs to receive answer
    received_ans = get_distance(from_lat, from_long, to_lat, to_long)

    assert round(expected_ans,2) == round(received_ans,2)