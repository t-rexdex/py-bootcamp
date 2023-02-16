# something something imports

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