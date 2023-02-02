# import sys
# sys.path.append("/Users/RexLAP/PycharmProjects/py_bootcamp/nile_project/")
from nile_project.main import * # not importing anything why did it lose access to the path

class TestTrip:  
      # simple test case for driver class handles floats and ints
    def test_details(self):
        driver1 = Driver(4, 10)
        t_test = Trip(200, driver1, 15.0)
        assert (200, driver1, float(15))  == (t_test.cost, t_test.driver, t_test.drive_cost)
driver1 = Driver(4, 10)
driver2 = Driver(7, 20)

def test_calculate_revenue_made_during_trip():
    trip1 = Trip(200, driver1, 15)
    assert 185 == trip1.cost - trip1.drive_cost
    
    trip2 = Trip(300, driver2, 40)  
    
def test_m():
    expected_ans = 445 
    trip1 = Trip(200, driver1, 15)    
    trip2 = Trip(300, driver2, 40)
    returned_ans = calculate_money_made(trip_id_1= trip1, trip_id_2= trip2)
    assert expected_ans == returned_ans
