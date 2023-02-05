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
            print('Creating database and establishing connection')
        con = sqlite3.connect(path_for_file)
    except Exception as e:
        print(e)

    return con
        
def create_table(con, table_name, *args):
    try:
        c = con.cursor()
        table_stuff = f'CREATE TABLE {table_name}(# how do i insert args into here appropriately?  )'
        # huy showed me how to map this as a dictionary! lets use this method
        c.execute()
    except Exception as e:
        print(e)
# create cursor object
# create table maybe have some logic if this table exists currently
def create_table_with_fields(*args):
    '''
        Function exists to take arguments and use those to create a table with those arguments as column headers
        need to convert this into use with sqlite
    '''
    table_lst = []
    for arg in args:
        table_lst.append(arg)
    # table_dict = {}
    # for arg in args:
    #     table_dict[arg] = None
    return table_lst # returns a header for table



def need_to_contain():        
# fill table 
    n = 100 # number of rows in the table 
    trip_ids = list(range(1,n+1)) # 1) trip_id: a unique number from 1 to 100,000. Meaning the table will have 100,000 unique records

    drivers = ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis'] # 2) name: a random string chosen from (alon, sarah, hailey, tyler, chaos, birtie, shiner, huy, jon, luis)
    drivers_long_list = random.choices(drivers, k=100) # allows list to populate with repetited items

    streets = ['Street_1', 'Street_2', 'Street_3']
    street_dict = {}
    for i in range(len(streets)): # goes from 0 > 1 > 2 
        m = streets[i] # street_i
        street_dict[m] = {}    # lst2 = streets[:i] + streets[i+1:]
        for j in range(len(streets)):
            n = streets[j]

            if n == m:
                continue


            if n not in street_dict:
                street_dict[m][n] = random.randint(50, 800) # currently populates a nested dictionary with values that do not match their permutated cousin
            else:
                street_dict[m][n] = street_dict[n][m]
            # in order to fix this i need to have another loop search in previous entries
    print(street_dict)
            #
    '''
    street 1 key is created. street 2 key is created next, in order for the street 2 key to match dict[street1][street2] 
    dict[street2] needs to look at dict[street1] 
    curretly the code is not allowing me
    '''

    print(street_dict)
 

    ''' 
    random functions to hopefully make sense soon 
    '''
    value = random.uniform(1, 10) # if i wanted a float between 1 and 10
    value_6 = random.randint(1, 6) # if i wanted a int between 1 and 10
    #
# print(tuple(assign_driver)[:200]) # print if you want to see the output but not necessary anymore
 
# now need to create something that goes through this list and places into the sql table

# with random.choices use something like the to go through a list of streets and create addresses 
def main():
    create_connection('./nile_project/dummy.db')

    dummy = create_table_with_fields('trip_id','name', 'source_location', 'destination_location', 'duration_mins' )
    print(dummy)


if __name__ == "__main__":
    main()   