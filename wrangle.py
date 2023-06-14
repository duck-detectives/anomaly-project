# Imports

import itertools
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import math
from sklearn import metrics
from random import randint
from matplotlib import style
import seaborn as sns
from sqlalchemy import text, create_engine





def acquire_logs(user=env.username, password=env.password, host=env.host):
    '''
    Function will utilize: username, password, & host from env file.
    Output: df containing curriculum log data from Codeup
    '''
    url = f'mysql+pymysql://{env.username}:{env.password}@{env.host}/curriculum_logs'
    query = '''
    select * 
    from logs
    join cohorts on logs.cohort_id = cohorts.id
    '''
    df = pd.read_sql(query, url)
    return df



def prep_logs(df):
    '''
    Input: curriculum logs df
    Actions: drop unused and duplicate columns, set datetime, reset index to datetime, set cohort id to int
    Output: cleaned df
    '''
    df = df.drop(columns=['id', 'slack', 'created_at', 'updated_at', 'deleted_at'])
    df['date_time'] = pd.to_datetime(df.date + ' ' + df.time)
    df = df.set_index('date_time')
    df = df.drop(columns=['date','time'])
    df.cohort_id = df.cohort_id.astype('int')
    df.start_date = df.start_date.astype('datetime64')
    df.end_date = df.end_date.astype('datetime64')
    df = df[(df.path != '/')
        & (df.path != 'toc')
        & (df.path != 'search/search_index.json')]
    return df














