from math import sin, cos, atan2, sqrt
from typing import Union

class TypeMismatchError(Error):
    print("Custom type mismatch")

# easy because it does not rely on any other functions that you already wrote
def get_distance(from_lat: int, from_long: int, to_lat: int, to_long: int) -> float:
    dlon = to_long - from_long
    
    try:
        dlat = from_lat - to_lat
    except TypeMismatchError: # cannot subtract two things if they are not the same type
        return None

    # new stuff

    a = (sin(dlat / 2)) ** 2 + cos(from_lat) * cos(to_lat) * (sin(dlon / 2)) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = a * c
    return distance


SHIPPING_PRICES = {
    "Ground": 1,
    "Priority": 1.6,
    "Overnight": 2.3,
}


def format_price(price: Union[int, float]) -> str:
    return "${0:.2f}".format(price)
