import sys
sys.path.append('./nile_project')
from table_population.table_main  import *
from pprint import pprint  as pp
import SQL_Helper


def main():
    '''
    I should probably refactor the project to create the trip log based on the layout of the fields_diction with the db schema 
    want to add cli, but need to focus on writing test for the sql_helper module
    what else what else
    '''
    number_of_total_streets = 50000
    total_number_of_trips = 100000
    min_distance = 50
    max_distance = 800
    drivers = ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis']
    print('Creating Street mapping')
    street_mapping = create_street_mapping(number_of_total_streets, min_distance, max_distance)
    print('\nStreet Mapping completed')
    tg1 = table_generation(min_distance, max_distance, total_number_of_trips, drivers)
    print('\nCreating Trip log from street mapping, and list of driver')
    trip_log = tg1.create_trip_log(street_mapping)
    print('\nCompleted trip log')
    tables = {
        'Trip_info': {
            'Trip_id': 'INTEGER PRIMARY KEY',
            'driver': 'TEXT',
            'start_location': 'TEXT', 
            'destination_location': 'TEXT', 
            'duration_in_mins': 'REAL', 
        } # data to create tables
    }

    con, c = SQL_Helper.create_connection('./nile_project/table_population/file.db') # establish connection
    print('\nCreating db table')
    SQL_Helper.create_table(con, c, tables) 
    print('Done with creating table, now beginning to insert trip log into db') 
    SQL_Helper.fill_table(con, c, trip_log, table_name = 'Trip_info')
    print('Script complete') 
    # for row in c.execute("select * from Trip_info"):
    #     print(row)




 



if __name__ == "__main__":
    main()   

