import sys
from pprint import pprint  as pp
import itertools

sys.path.append('./nile_project')
from table_population.table_main  import *
import SQL_Helper


def main():
    number_of_total_streets = 50000
    total_number_of_trips = 100000
    min_distance = 50
    max_distance = 800
    drivers = ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis']

    street_mapping = create_street_mapping(number_of_total_streets, min_distance, max_distance)
    tg1 = table_generation(min_distance, max_distance, total_number_of_trips, drivers)
    trip_log = tg1.create_trip_log(street_mapping)
    table_name = 'Trip_info'
    # lst = SQL_Helper.dict_to_list_for_import(trip_log)
    # print(lst)
    # outputs -> [[1, 'Alon', 'Street_5', 'Street_3', 200.0], [2, 'Huy', 'Street_1', 'Street_2', 50.0], 
    # [3, 'Jon', 'Street_3', 'Street_4', 200.0], [4, 'Chaos', 'Street_1', 'Street_3', 30.0], [5, 'Chaos', 'Street_2', 'Street_1', 50.0]]
    tables = {
        'Trip_info': {
            'Trip_id': 'INTEGER PRIMARY KEY',
            'name': 'TEXT',
            'source_location': 'TEXT', 
            'destination_location': 'TEXT', 
            'duration_mins': 'REAL', 
        } # data to create tables
    }

    # lst1 = SQL_Helper.dict_to_list_for_import(tables['Trip_info'])
    print()
    # outputs -> [['Trip_id', 'INTEGER PRIMARY KEY'], ['name', 'TEXT'], ['source_location', 'TEXT'], ['destination_location', 'TEXT'], ['duration_mins', 'REAL']]
    # for column, obj_type in lst1:
    # for array in lst:
    #     for value in array:
    #         print(value)
    #         print(type(value))   
    #         print('\n')
    # print('\n')
  # how to use this for loop to grab items from lst to insert properly in execute statement




    con, c = SQL_Helper.create_connection('./nile_project/table_population/file.db') # establish connection
    SQL_Helper.create_table(con, c, tables) 
    # SQL_Helper.print_table_fields(con, c, tables) 
    SQL_Helper.fill_table(con, c, trip_log, table_name = 'Trip_info')

    for row in c.execute("select * from Trip_info"):
        print(row)




 



if __name__ == "__main__":
    main()   

