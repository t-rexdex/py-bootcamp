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
    street_dict = {}
    def __init__(self, min_distance: int | float, max_distance: int | float, number_of_total_streets: int, total_number_of_trips: int, drivers_list: list ) -> None:
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.number_of_total_streets = number_of_total_streets
        self.total_number_of_trips = total_number_of_trips
        self.drivers_list = drivers_list
        self.street_dict = self.create_street_alt()

    def __repr__(self):
        return f'This trip log contains {self.total_number_of_trips} trips made between {self.number_of_total_streets} addresses'

    def get_distance():
        pass

    def get_delivery_time(self, distance: int, driver: str) -> float:
        '''
        Retrieves delivery time based on the driver and trip distance. 
        It is meant to be used inside the create trip log folder
        I might actually make this into two functions
        '''
        
        if distance >= 50 and distance <= 100: # need to changes that 50 to min(street_distance) or something like that
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
    def create_street_alt(self) -> dict:
        '''
        Creating a basic street mapping dictionary with distances between each street
        '''
        streets = []
        for street_number in range(self.number_of_total_streets):
            streets.append('Street_' + str(street_number+1))
        street_dict = {}
        for i in range(len(streets)): # goes from 0 > 1 > 2 
            m = streets[i] # street_i
            street_dict[m] = {}   
            for j in range(len(streets)):
                n = streets[j]

                if n == m:
                    continue

                if n not in street_dict: 
                    street_dict[m][n] = random.randint(self.min_distance, self.max_distance) # currently populates a nested dictionary with values that do not match their permutated cousin

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
        # print out a pair of streets
            driver = random.choice(self.drivers_list)
            pair= random.sample(sorted(self.street_dict), 2)
            try:
                trip_log[trip + 1] = (driver, pair[0], pair[1], self.get_delivery_time(self.street_dict[pair[0]][pair[1]], driver))
            except:
                trip_log[trip + 1] = (driver, pair[0], pair[1], self.get_delivery_time(self.street_dict[pair[1]][pair[0]], driver))

    

            
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

    trip_log = table_generation.create_trip_log(100000, ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis'], table_generation.create_street_alt(500, 60, 800))

    # print('This is true log')

    print('Log is completed')
    # pprint.pprint(trip_log)





if __name__ == "__main__":
    main()   




