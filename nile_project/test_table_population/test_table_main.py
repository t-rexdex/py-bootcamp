import pytest
import sys
sys.path.append('./nile_project')
from table_population.table_main  import table_generation as tg
import pprint

drivers = ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis']
# street = table_main.create_street_alt(500, 60, 800)
# trip_log = table_main.create_trip_log(10000, drivers, table_main.create_street_alt(500, 60, 800))
# src.main()
tg1 = tg(50,800,5,5, drivers)
# street_mapping = tg1.street_dict
print(tg1.street_dict['Street_5'])
# pprint.pprint(trip_log1.street_dict['Street_480'])


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
    assert len(tg1.street_dict.keys()) == expected_ans

    # Testing that the string creation of the keys properly numbers
    expected_ans = ['Street_1', 'Street_2', 'Street_3', 'Street_4', 'Street_5']
    assert list(tg1.street_dict.keys()) == expected_ans

    # Testing if last key is empty to save memory space with larger generations sizes
    expected_ans = {}
    assert tg1.street_dict['Street_5'] == expected_ans
   
# how do i break program to receive delivery_time = None?
    # maybe test that some locations exist within an another key
    # maybe use a test to find the minimum distance, max distance





