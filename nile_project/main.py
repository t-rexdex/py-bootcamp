from nile_project.nile import get_distance, format_price, SHIPPING_PRICES


class Driver:
    def __init__(self, speed, salary):
        self.speed = speed
        self.salary = salary

    def __repr__(self):
        return "Nile Driver speed {} salary {}".format(self.speed, self.salary)


class Trip:
    def __init__(self, cost, driver, drive_cost):
        self.cost = cost
        self.driver = driver
        self.drive_cost = drive_cost

class Unreal_Lat_or_Long(Exception):
    def __init__(self, from_lat, from_long, to_lat, to_long):
        self.from_lat = from_lat
        self.from_long = from_long
        self.to_lat = to_lat
        self.to_long = to_long

    def __str__(self):
        return 'Got {self.from_lat}, {self.from_long} and {self.to_lat}, {self.to_long} expected value between (-90, 90) for the latitude and (-180, 180) for longitude'

from_coords = (5, 6)
to_coords = (9, 7)
# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords, shipping_type="Overnight"):
    from_lat, from_long = from_coords
    to_lat, to_long = to_coords
    distance = get_distance(from_lat, from_long, to_lat, to_long)
    price = distance * SHIPPING_PRICES[shipping_type]
    return format_price(price)


# Define calculate_driver_cost() here
def calculate_cheapest_driver_cost(distance, *args):
    cheapest_driver = None
    cheapest_driver_price = None
    for driver in args:
        driver_time = distance / driver.speed
        price_for_driver = driver.salary * driver_time
        if cheapest_driver is None:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
        elif price_for_driver < cheapest_driver_price:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver

    return cheapest_driver_price, cheapest_driver


# Define calculate_money_made() here
def calculate_money_made(**trips):
    total_money_made = 0
    for trip_id, trip in trips.items():

        trip_revenue = trip.cost - trip.drive_cost

        total_money_made += trip_revenue
    return total_money_made
