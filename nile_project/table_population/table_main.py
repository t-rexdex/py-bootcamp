import random
import sqlite3
import itertools
import os
import pprint
random.seed(420) # importing for reproducibility

def create_connection(path_for_file: str) -> object : 
    # create a way to test if file exists in directory
    try:
        if os.path.isfile(path_for_file):
            print('File already exists. Reestablishing connection')
        else:
            print('Creating database and establishing a connection')
        con = sqlite3.connect(path_for_file)
        c = con.cursor()
    except Exception as e:
        print(e)

    return con, c
        
    
def create_table(con, c, fields_dict: dict):
    '''
    Need to create a test file for testing these methods
    '''

    try:
        for table in fields_dict:
            columns = "(" + ",\n".join(["{} {}".format(k,v) for k,v in fields_dict[table].items()]) + ")"
            c = con.cursor()
            c.execute("CREATE TABLE " + table + "\n" + columns) # there has to be a better way to implement the name of this table
            con.commit()
            # print(f'Table {table} was created with the following fields \n{columns}')
            print('Table was sucessfully created')
    except Exception as e:
        print(e)


def print_table_fields(con, c, fields_dict): # need to rework may need to also add the cursor, maybe create a class so self can be thrown into the attributes
    '''
    Not perfectly executed, deciding if this is necessary or not, 
    It is mostly for debugging and my personal use.
    '''
    for table in fields_dict:
        print(f'\nColumns in {table} table:')
        data=c.execute("SELECT * FROM " + table ) # need to fix this line so sqlite can properly call the correct table
        for column in data.description:
            print(column[0])
class table_generation():
    def __init__(self, min_distance: int | float, max_distance: int | float, number_of_total_streets: int, total_number_of_trips: int, drivers_list: list ) -> None:
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.number_of_total_streets = number_of_total_streets
        self.total_number_of_trips = total_number_of_trips
        self.drivers_list = drivers_list
        self.street_dict = self.create_street_mapping() # huy raised a decent point about this existing within the class
        # street locations are static, with the exception of adding new locations
        # so i think i will remove  the create_street_alt() from the class

    def __repr__(self):
        return f'This trip log contains {self.total_number_of_trips} trips made between {self.number_of_total_streets} addresses'

    def get_distance(self, start_location, end_location):

        try :
            distance = self.street_dict[start_location][end_location]
        except:
            distance = self.street_dict[end_location][start_location]
        
        return distance
            

    def get_delivery_time(self, distance: int, driver: str) -> float:
        '''
        Retrieves delivery time based on the driver and trip distance. 
        It is meant to be used inside the create trip log folder
        I might actually make this into two functions
        '''
        
        if distance >= self.min_distance and distance <= 100: # need to changes that 50 to min(street_distance) or something like that
            delivery_time = 50.0

        elif distance > 100 and distance <= 200:
            delivery_time = 80.0

        elif distance > 200 and distance <= 300:
            delivery_time = 250.0

        elif distance > 300:
            if driver in ('Chaos', 'Bertie', 'Shiner'):
                delivery_time = 30.0

            elif 'e' in driver and distance < 350: #name has no letter 'e' and distance below 350: 150
                delivery_time = 150.0
            
            elif len(driver) < 4 and distance < 420: #the number of letters in name is no more than 4 and distance below 420: 420
                delivery_time = 420.0

            else:
                delivery_time = 200.0
        else:
            delivery_time = None

        return delivery_time

    # need to update create street_mapping and delivery time methods to include min and max distances IE need to create a class for this
    def create_street_mapping(self) -> dict:
        '''
        Creating a basic street mapping dictionary with distances between each street
        '''
        streets = []
        # can probably condense this whole function further 
        for street_number in range(self.number_of_total_streets): # want to condense lines 106 and 107
            streets.append('Street_' + str(street_number+1))
        street_dict = {}
        for outer_loop in range(len(streets)): # goes from 0 > 1 > 2 
            starting_loc = streets[outer_loop] # street_i
            street_dict[starting_loc] = {}   
            for inner_loop in range(len(streets)):
                ending_loc = streets[inner_loop]

                if ending_loc == starting_loc:
                    continue

                if ending_loc not in street_dict: 
                    street_dict[starting_loc][ending_loc] = random.randint(self.min_distance, self.max_distance) 

        return street_dict


    def create_trip_log(self) -> dict :
        ''' 
        Need to come up with a way that inserts data into the database or maybe just create a log for further use
        I know the current way i have the code working is that there is a number of items being stored in memory
        total_number_of_trips: int to represent the amount of trips created also resulting in the amount of data to insert into the database 
        driver_list :list a list of drivers to choose from 
        street_dict :dict for street mapping representation

        returns a dictionary that has the following fields:
        Trip_id
        Driver
        Start_location
        End_location
        Distance
        Time
        '''

        trip_log = {}
        for trip in range(self.total_number_of_trips):
            driver = random.choice(self.drivers_list)
            start,end= random.sample(sorted(self.street_dict), 2)
            trip_log[trip + 1] = (driver, start, end, self.get_delivery_time(self.get_distance(start, end), driver))
            
        return trip_log

 
# now need to create something that goes through this list and places into the sql table

def main():
    # con, c = create_connection('./nile_project/table_population/file.db') # establish connection

    # tables = {
    #     'Trip_info': {
    #         'Trip_id': 'str PRIMARY KEY',
    #         'name': 'str',
    #         'source_location': 'str', 
    #         'destination_location': 'str', 
    #         'duration_mins': 'float', 
    #     } # data to create tables
    # }


    # create_table(con, c, tables) 

    # print_table_fields(con, c, tables) 


    # ##### Playing with the code 
    # print('Creating Street mapping dictionary')
    # street_mapping = create_street_mapping_dictionary(5000) # mapping created need to insert this into db
    # street_mapping = create_street_alt(500, 60, 800)
    # print('Successfully created mapping dictionary')

    # print('\n\n\n\n')
    print('Creating Trip log dictionary')

    trip_log = table_generation.create_trip_log(100000, ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis'], table_generation.create_street_mapping(500, 60, 800))

    # print('This is true log')

    print('Log is completed')
    # pprint.pprint(trip_log)





if __name__ == "__main__":
    main()   




