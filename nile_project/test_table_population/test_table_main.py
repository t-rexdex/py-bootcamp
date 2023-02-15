import pytest
import sys
sys.path.append('./nile_project')
from table_population.table_main  import table_generation as tg
import pprint

drivers = ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis']
# street = table_main.create_street_alt(500, 60, 800)
# trip_log = table_main.create_trip_log(10000, drivers, table_main.create_street_alt(500, 60, 800))
# src.main()
trip_log1 = tg(50,800,500,10000, drivers)
trip = trip_log1.create_trip_log()
# pprint.pprint(trip_log1.street_dict['Street_480'])
print(tg.get_delivery_time(trip_log1, 80, 'Alon'))

def test_delivery_time():
    assert tg.get_delivery_time(trip_log1, 80, 'Alon') == 50.0 # check first if statement
    assert tg.get_delivery_time(trip_log1, 200.0, 'Alon') == 80.0 # check second if statement
    assert tg.get_delivery_time(trip_log1, 201, 'Alon') == 250.0 # check third if statement
    assert tg.get_delivery_time(trip_log1, 301, 'Chaos') == 30.0 # check first nested if statement
    assert tg.get_delivery_time(trip_log1, 301, 'Hailey') == 150.0 # check second nested if statement
    assert tg.get_delivery_time(trip_log1, 419, 'Huy') == 420.0 # check first if statement
    assert tg.get_delivery_time(trip_log1, 325, 'Alon') == 200.0 # check first if statement
# how do i break program to receive delivery_time = None?






