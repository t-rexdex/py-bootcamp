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
    may need to reinsert the table that it used to create fields to fill in the (insert into table_name VALUES() columns)
    having issues with the columns string. 
    outputing as: (1, Alon, Street_5, Street_3, 200.0)
    needs to be: (1, 'Alon', 'Street_5', 'Street_3', 200.0)
    what do i need to do the have those parts of the string to be read correctly

    # you can iterate through lst[i]


            fields = "(" + ",   ".join(["{}".format(k) for k in list(fields_dict[table_name].keys())]) + ")"
            columns = "(" + "".join(f"{outerlst[0]}, {outerlst[1]}, {outerlst[2]}, {outerlst[3]}, {outerlst[4]}") + ")"
            c = con.cursor()
            c.execute("INSERT INTO " + table_name + fields + "\nVALUES" + columns +";") 
            # outputing as: (1, Alon, Street_5, Street_3, 200.0)
            # needs to be: (1, 'Alon', 'Street_5', 'Street_3', 200.0) 
            # hints it can be related to using fields_dict i believe if i do this itll allow me to use executemany
            # maybe haing something that looks into fields dict at that index and if type is text then the in the trip log
            # we should have the names, start and end should have an output to match 'Driver' 'Street_start' 'Street_end'
            # that and we may also need to change the way the outerlist is read?
                # print(tables['Trip_info'].values())
                # print(tables['Trip_info'].keys())
                # print(list(tables['Trip_info'].keys())[3:])


        con.commit()


# INSERT INTO table (column1,column2 ,..)
# VALUES( value1,	value2 ,...);
'''
    # lst = dict_to_list_for_import(some_dict)
    c.executemany("INSERT INTO " + table_name + " VALUES (?, ?, ?, ?, ?)", dict_to_list_for_import(some_dict))
    con.commit()