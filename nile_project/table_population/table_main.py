import random
import sqlite3
import itertools
import os
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

def print_table_data():
    '''
    samething as above, trying to decide if this method is necessary
    '''
    pass


def create_street_mapping_dictionary(number_of_total_streets: int) -> dict:
    '''
    Creating a basic street mapping dictionary with distances between each street
    '''
    streets = []
    for street_number in range(number_of_total_streets):
        streets.append('Street_' + str(street_number+1))
    street_dict = {}
    for i in range(len(streets)): # goes from 0 > 1 > 2 
        m = streets[i] # street_i
        street_dict[m] = {}    # lst2 = streets[:i] + streets[i+1:]
        for j in range(len(streets)):
            n = streets[j]

            if n == m:
                continue


            if n not in street_dict:
                street_dict[m][n] = random.randint(50, 800) # currently populates a nested dictionary with values that do not match their permutated cousin
            else:
                street_dict[m][n] = street_dict[n][m]
    return street_dict

def create_trip_log( 
    total_number_of_trips: int, 
    driver_list: list, 
    street_dict: dict
    ) -> tuple| list :
    ''' 
    Need to come up with a way that inserts data into the database or maybe just create a log for further use
    I know the current way i have the code working is that there is a number of items being stored in memory
    total_number_of_trips: int to represent the amount of trips created also resulting in the amount of data to insert into the database 
    driver_list :list a list of drivers to choose from 
    street_dict :dict for street mapping representation
    '''
    trip_log = {}
    trip_ids = list(range(1, total_number_of_trips+1))
    drivers_long_list = random.choices(driver_list, k = total_number_of_trips) # allows list to populate with repetited items
    mapping_start_locations = random.choices(list(street_dict.keys()), k = total_number_of_trips)
    mapping_end_locations = random.choices(list(street_dict.keys()), k = total_number_of_trips)    
    for trip in range(total_number_of_trips):
        trip_log[trip + 1] = { drivers_long_list[trip], mapping_start_locations[trip], mapping_end_locations[trip] }

    return trip_log

def need_to_contain():        
# fill table 
    n = 100 # number of rows in the table 
    trip_ids = list(range(1,n+1)) # 1) trip_id: a unique number from 1 to 100,000. Meaning the table will have 100,000 unique records

    drivers = ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis'] # 2) name: a random string chosen from (alon, sarah, hailey, tyler, chaos, birtie, shiner, huy, jon, luis)

   
 

    ''' 
    random functions to hopefully make sense soon 
    '''
    value = random.uniform(1, 10) # if i wanted a float between 1 and 10
    value_6 = random.randint(1, 6) # if i wanted a int between 1 and 10
    #
# print(tuple(assign_driver)[:200]) # print if you want to see the output but not necessary anymore
 
# now need to create something that goes through this list and places into the sql table

# with random.choices use something like the to go through a list of streets and create addresses 


def main():
    # con, c = create_connection('./nile_project/table_population/file.db') # establish connection

    tables = {
        'Trip_info': {
            'Trip_id': 'str PRIMARY KEY',
            'name': 'str',
            'source_location': 'str', 
            'destination_location': 'str', 
            'duration_mins': 'float', 
        } # data to create tables
    }


    # create_table(con, c, tables) 

    # print_table_fields(con, c, tables) 


    # ##### Playing with the code 
    street_dict_mapping = create_street_mapping_dictionary(500) # mapping created need to insert this into db
    trip_log = create_trip_log(10, ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis'], street_dict_mapping)
    # for some reason the dictionary that im going to use to populate the db is not inserting in the right order
    print(trip_log)


if __name__ == "__main__":
    main()   

# driver_list = ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis']
# total_number_of_trips = 100
# drivers_long_list = random.choices(driver_list, k = total_number_of_trips) # allows list to populate with repetited items
# mapping_start_locations = random.choices(list(street_dict_mapping.keys()), k = 10)
# mapping_end_locations = random.choices(list(street_dict_mapping.keys()), k = 10)
# trip_ids = list(range(1, total_number_of_trips+1))
# print(mapping_start_locations)
# print('This is end locations')
# print(mapping_end_locations)
