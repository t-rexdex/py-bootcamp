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
    Also need to create a test file for testing these methods
    '''

    try:
        for table in fields_dict:
            columns = "(" + ",\n".join(["{} {}".format(k,v) for k,v in fields_dict[table].items()]) + ")"
            c = con.cursor()
            c.execute("CREATE TABLE " + table + "\n" + columns) # there has to be a better way to implement the name of this table
            con.commit()
            print(f'Table {table} was created with the following fields \n{columns}')
    except Exception as e:
        print(e)

def print_table_fields(fields_dict: dict): # need to rework may need to also add the cursor, maybe create a class so self can be thrown into the attributes
    for table in fields_dict:
        print(f'\nColumns in {table} table:')
        data=c.execute('''SELECT * FROM your_mom''') # need to fix this line so sqlite can properly call the correct table
        for column in data.description:
            print(column[0])


def main():
    con, c = create_connection('./nile_project/table_population/file.db') # establish connection

    tables = {
        'test': {
            'Trip_id': 'str PRIMARY KEY',
            'name': 'str',
            'source_location': 'str', 
            'destination_location': 'str', 
            'duration_mins': 'float', 
        } # data to create tables
    }



if __name__ == "__main__":
    main()   


    # create_table(con, c, tables) # trying to create table that fills in information using a dictionary, primary key, and primary key type
    ##### Playing with the code 
    # c.execute("""
    #     INSERT INTO your_mom VALUES
    #         ('Tyler', 'Dexter', '1', 'Coupe', 60),
    #         ('Huy', 'Tran', '2', 'Sedan', 50)
    # """)
    # con.commit()
    # drive_response = c.execute('SELECT * FROM your_mom')
    # print(drive_response.fetchall())
    # print('\n') 