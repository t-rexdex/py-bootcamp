import sys
from Generator import table_generation, create_street_mapping, get_distance
from SQL_Helper import mysqlite3 as ms3

def main():
# need to contain these in argparse
######################################################
    number_of_total_streets = int(sys.argv[1])
    total_number_of_trips = int(sys.argv[2])
    min_distance = float(sys.argv[3])
    max_distance = float(sys.argv[4])
    drivers = ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis']
######################################################
    street_mapping = create_street_mapping(number_of_total_streets, min_distance, max_distance)

    tg1 = table_generation(min_distance, max_distance, total_number_of_trips, drivers)

    trip_log = tg1.create_trip_log(street_mapping)

    table = {
        'Trip_info': {
            'Trip_id': 'INTEGER PRIMARY KEY',
            'driver': 'TEXT',
            'start_location': 'TEXT', 
            'destination_location': 'TEXT', 
            'duration_in_mins': 'REAL', 
        }
    }

    with ms3() as db:
        db.create_table(table)
        db.executemany(trip_log)

if __name__ == "__main__":
    main()   
