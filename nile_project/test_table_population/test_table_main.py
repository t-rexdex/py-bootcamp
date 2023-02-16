import pytest
import sys
sys.path.append('./nile_project')
from table_population.table_main  import *
import pprint


'''
It is important to have these default parameters for the random seed to populate the correct
values
number_of_total_streets = 5
total_number_of_trips = 5
min_distance = 50
max_distance = 800
drivers = ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis']
'''

number_of_total_streets = 5
total_number_of_trips = 5
min_distance = 50
max_distance = 800
drivers = ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis']

street_mapping = create_street_mapping(number_of_total_streets, min_distance, max_distance)
tg1 = table_generation(min_distance, max_distance, total_number_of_trips, drivers)
print(street_mapping)
# print(tg1.street_dict['Street_5'])
pprint.pprint(tg1.create_trip_log(street_mapping))


@pytest.mark.parametrize('distance, driver ,expected_result',[
    (50,'Alon', 50.0),
    (200.0, 'Alon', 80.0),
    (201, 'Huy', 250),
    (330, 'Chaos', 30.0),
    (419, 'Huy', 420.0),
    (325, 'Alon',200.0),
    (325, 'Hailey', 150.0) ] )
def test_delivery_time(distance, driver, expected_result):
    assert tg1.get_delivery_time(distance, driver) == expected_result # check first if statement


def test_create_street_mapping():
    # Testing for the amount of keys be the same as line 11, the third argument 5
    expected_ans = 5
    assert len(street_mapping.keys()) == expected_ans

    # Testing that the string creation of the keys properly numbers
    expected_ans = ['Street_1', 'Street_2', 'Street_3', 'Street_4', 'Street_5']
    assert list(street_mapping.keys()) == expected_ans

    # Testing if last key is empty to save memory space with larger generations sizes
    expected_ans = {}
    assert street_mapping['Street_5'] == expected_ans


@pytest.mark.parametrize('start_location, end_location, expected_result',[
    ('Street_1', 'Street_2', 76),
    ('Street_2','Street_4', 147),
    ('Street_4', 'Street_2', 147)]) 
def test_get_distance(start_location, end_location, expected_result):
   assert get_distance(street_mapping, start_location, end_location) == expected_result
   






