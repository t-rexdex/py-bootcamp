import argparse
from Generator import table_generation, create_street_mapping, get_distance
from SQL_Helper import mysqlite3 as ms3

def main():
    # definitely need to condense these args 
    parser = argparse.ArgumentParser()
    parser.add_argument('--streets')
    parser.add_argument('--trips')
    parser.add_argument('--min_distance')
    parser.add_argument('--max_distance')
    args = vars(parser.parse_args()) # if im using this and it becomes a dict perhaps I should refactor once again to take advantage of the new format

    number_of_total_streets = args['streets']
    total_number_of_trips = args['trips']
    min_distance = args['min_distance']
    max_distance = args['max_distance']
    drivers = ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis']
    print(type(args))
    # street_mapping = create_street_mapping(number_of_total_streets, min_distance, max_distance)

    # tg1 = table_generation(min_distance, max_distance, total_number_of_trips, drivers)

    # trip_log = tg1.create_trip_log(street_mapping)

    # table = {
    #     'Trip_info': {
    #         'Trip_id': 'INTEGER PRIMARY KEY',
    #         'driver': 'TEXT',
    #         'start_location': 'TEXT', 
    #         'destination_location': 'TEXT', 
    #         'duration_in_mins': 'REAL', 
    #     }
    # }

    # with ms3() as db:
    #     db.create_table(table)
    #     db.executemany(trip_log)

if __name__ == "__main__":
    main()   
