import os
import pandas as pd 
import numpy as np

import re

from sklearn.model_selection import train_test_split
import sklearn.preprocessing

import env


# setting connectiong to sequel server using env
def get_connection(db, user=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'



##################
 
# acquiring telco data using a different function

def get_logs_data(get_connection):
    filename = "logs.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col = 0)
    
    else:
        
    # read the SQL query into a dataframe
        df = pd.read_sql(
    
        '''
        
       SELECT date,
       path as endpoint,
       user_id,
       cohort_id,
       ip as source_ip
        FROM logs;
        
        ''', get_connection('curriculum_logs'))

    # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

    # Return the dataframe to the calling code
    return df 


##################
 
# acquiring groceries using a different function

def get_groceries_data(get_connection):
    filename = "grocs.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col = 0)
    
    else:
        
    # read the SQL query into a dataframe
        df = pd.read_sql(
    
        '''
        
      select * from grocery_customers

        ''', get_connection('grocery_db'))

    # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

    # Return the dataframe to the calling code
    return df 