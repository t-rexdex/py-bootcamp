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
        
    
def create_table(con, c, columns_dict: dict):
    '''
    Not fully functioning, need to refactor so that the create table function can pull the primary key for EACH table instead of only assigning
    for a single table like I am currently doing.
    Also need to create a test file for testing these methods
    '''

    try:
        for table in columns_dict:
            columns = "(" + ",\n".join(["{} {}".format(k,v) for k,v in columns_dict[table].items()]) + ")"
            c = con.cursor()
            c.execute("CREATE TABLE " + table + "\n" + columns) # there has to be a better way to implement the name of this table
            con.commit()
            print(f'Table {table} was created with the following fields \n{columns}')
    except Exception as e:
        print(e)



def main():
    con, c = create_connection('./nile_project/table_population/dummy.db') # establish connection

    tables = {
        'your_mom': {
            'Trip_id': 'str PRIMARY KEY',
            'name': 'str',
            'source_location': 'str', 
            'destination_location': 'str', 
            'duration_mins': 'float', 
        } # data to create tables
    }


    create_table(con, c, tables) # trying to create table that fills in information using a dictionary, primary key, and primary key type
    ##### Playing with the code 



if __name__ == "__main__":
    main()   

# columns_dict = {
#     'Trip_info': {
        # 'Trip_id': 'str PRIMARY KEY',
#         'name': 'str',
#         'source_location': 'str', 
#         'destination_location': 'str', 
#         'duration_mins': 'float', 
#     } # data to create tables
# }

# for table in columns_dict:
#     columns = "(" + ",\n".join(["{} {}".format(k,v) for k,v in columns_dict[table].items()]) + ")"
#     print(type(table))