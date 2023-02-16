import random
import itertools

random.seed(420) # importing for reproducibility


###########################################################################################            

def create_street_mapping(number_of_total_streets, min_distance, max_distance) -> dict:
    '''
    Creating a basic street mapping dictionary with distances between each street
    '''
    streets = []
    # can probably condense this whole function further 
    for street_number in range(number_of_total_streets): # want to condense lines 57 & 58
        streets.append('Street_' + str(street_number+1))
    street_mapping = {}
    for outer_loop in range(len(streets)):  
        starting_loc = streets[outer_loop]
        street_mapping[starting_loc] = {}   
        for inner_loop in range(len(streets)):
            ending_loc = streets[inner_loop]

            if ending_loc == starting_loc:
                continue

            if ending_loc not in street_mapping: 
                street_mapping[starting_loc][ending_loc] = random.randint(min_distance, max_distance) 
            # i believe these if loops should be something to cover an else statement
    return street_mapping 


def get_distance(street_mapping, start_location, end_location):
    try :
        distance = street_mapping[start_location][end_location]
    except:
        distance = street_mapping[end_location][start_location]
    
    return distance
            


class table_generation():
    def __init__(self, min_distance: int | float, max_distance: int | float, total_number_of_trips: int, drivers_list: list ) -> None:
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.total_number_of_trips = total_number_of_trips
        self.drivers_list = drivers_list


    def __repr__(self):
        return f'This trip log contains {self.total_number_of_trips} trips made between {self.number_of_total_streets} addresses'


    def get_delivery_time(self, distance: int, driver: str) -> float:
        '''
        Retrieves delivery time based on the driver and trip distance. 
        It is meant to be used inside the create trip log folder
        I might actually make this into two functions
        '''
        
        if distance >= self.min_distance and distance <= 100: 
            delivery_time = 50.0

        elif distance > 100 and distance <= 200:
            delivery_time = 80.0

        elif distance > 200 and distance <= 300:
            delivery_time = 250.0

        elif distance > 300:
            if driver in ('Chaos', 'Bertie', 'Shiner'):
                delivery_time = 30.0

            elif 'e' in driver and distance < 350:
                delivery_time = 150.0
            
            elif len(driver) < 4 and distance < 420:
                delivery_time = 420.0

            else:
                delivery_time = 200.0
        else:
            delivery_time = None

        return delivery_time



    def create_trip_log(self, street_mapping) -> dict :
        ''' 
        total_number_of_trips: int to represent the amount of trips created also resulting in the amount of data to insert into the database 
        driver_list :list a list of drivers to choose from 
        street_dict :dict for street mapping representation
        returns a dictionary that has the following fields:
        Trip_id:
        {
        Driver
        Start_location
        End_location
        Time 
        }
        '''

        trip_log = {}
        for trip in range(self.total_number_of_trips):
            driver = random.choice(self.drivers_list)
            start,end= random.sample(sorted(street_mapping), 2)
            trip_log[trip + 1] = (driver, start, end, self.get_delivery_time(get_distance(street_mapping, start, end), driver))
            
        return trip_log
