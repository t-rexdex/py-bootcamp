import random
import sqlite3
import numpy as np
random.seed(420) # importing for reproducibility


# create sqlite functions
# create connection
# create cursor object
# create table maybe have some logic if this table exists currently
# fill table 
n = 100 # number of rows in the table 
trip_ids = list(range(1,n+1)) # 1) trip_id: a unique number from 1 to 100,000. Meaning the table will have 100,000 unique records

drivers = ['Alon', 'Sarah', 'Hailey', 'Tyler', 'Chaos', 'Bertie', 'Shiner', 'Huy', 'Jon', 'Luis'] # 2) name: a random string chosen from (alon, sarah, hailey, tyler, chaos, birtie, shiner, huy, jon, luis)
drivers_long_list = random.choices(drivers, k=100) # allows list to populate with repetited items
streets_dict = {}
for i in range(int(n/2)):
    streets_dict['Street_' + str(i+1)] = i+1 
    # need to create a sub dictionary that randomly picks two other streets but also matches this data in the dict

# 3) source_location: a random string chosen from the above distance keys
source_location = random.choices(tuple(streets_dict), k=100) # why can i not assign this to a variable? # need to ask huy or google some more

# 4) destination_location: a random string chosen at distance[source_location]
#   For example, if source_location is randomly chosen as 'street_1', destination_location is randomly chosen as either 'street_2' or 'street_3'

# 5) duration_mins: a random float that depends on distance (which is deducted from step 3 and 4) with the following rules, in the following order of priorities:
# If distance is from 50 to 100: 50.0
# If distance is from 100 to 200: 80.0
# If distance is from 200 to 300: 250.0
# If distance is above 300: 
# If name is shiner or birtie or chaos: 30.0
# If name has no letter 'e' and distance below 350: 150
# If the number of letters in name is no more than 4 and distance below 420: 420
# else: 200.0 

# create street dictionary

''' 
random functions to hopefully make sense soon 
'''
value = random.uniform(1, 10) # if i wanted a float between 1 and 10
value_6 = random.randint(1, 6) # if i wanted a int between 1 and 10
#
# print(tuple(assign_driver)[:200]) # print if you want to see the output but not necessary anymore
 
# now need to create something that goes through this list and places into the sql table

# with random.choices use something like the to go through a list of streets and create addresses 