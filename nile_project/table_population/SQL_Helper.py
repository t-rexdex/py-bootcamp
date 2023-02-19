import sqlite3
import os

def create_connection(path_for_file: str) -> object : 
    # create a way to test if file exists in directory
    try:
        if os.path.isfile(path_for_file):
            os.remove(path_for_file)
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
     tables = {
        'Trip_info': {
            'Trip_id': 'int PRIMARY KEY',
            'name': 'str',
            'source_location': 'str', 
            'destination_location': 'str', 
            'duration_mins': 'float', 
        } # data to create tables
    }
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


def check_size_of_insert_table_and_trip_log(table, trip_log):
    '''
    possibly create this method to check if values will successfully enter into db based on called table and trip_log
    '''
    pass


def dict_to_list_for_import(some_dict: dict) -> list:
    lst = []
    for tple in some_dict.items():
        outerlst = []   
        for item in tple:
            if type(item) == tuple:
                for i in item:
                    outerlst.append(i)
            else:
                outerlst.append(item)
        lst.append(outerlst)
    return lst

def fill_table(con, c, some_dict, table_name = ""):
    '''
    Create a method to take in a dictionary and insert that into a table 
    takes in a dictionary but converts to list for my comprehension
    '''

    c.executemany("INSERT INTO " + table_name + " VALUES (?, ?, ?, ?, ?)", dict_to_list_for_import(some_dict))
    con.commit()