import sqlite3
import os

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