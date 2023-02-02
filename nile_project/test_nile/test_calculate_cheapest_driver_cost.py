from nile_project.main import * # not importing anything why did it lose access to the path


class TestDriver:  
      # simple test case for driver class
    def test_details(self):
        d_test = Driver(4, 10)
        assert (4, 10)  == (d_test.speed, d_test.salary)
        # test repr method
        expected_ans =  'Nile Driver speed 4 salary 10'
        assert expected_ans == repr(d_test)

    # testing class can accept float and ints
        d_test = Driver(float(4), 10)
        assert (4.0, 10)  == (d_test.speed, d_test.salary)

        
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

    # handles ints and floats
    expected_ans =10
    driver_time_test = 1
    driver_price_test = driver_test.salary * driver_time_test
    assert expected_ans == driver_price_test
    
def test_calulate_smaller_driver_cost():
    # i know is a better way to call this stuff for the test
    driver2_test = Driver(7, 20)
    expected_ans = driver_test
    returned_price, returned_driver = calculate_cheapest_driver_cost(expected_distance, driver_test, driver2_test)
    assert expected_ans == returned_driver

    # checking cheapest_price gets correctly called from the two drivers
    expected_ans = 1.1281
    assert expected_ans == round(returned_price, 4)
