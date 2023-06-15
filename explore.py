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
from matplotlib import style
import seaborn as sns



############### QUESTION 1 ##################

def most_accessed_per_program(logs):
    ''' Takes in the prepared access logs dataframe and returns a list of the top five lessons accessed per program.'''
    path_df = logs.path.str.split('/', 2, expand=True)
    logs = pd.concat([logs, path_df], axis = 1)
    logs = logs.rename(columns = {0 : 'main_path'
                          ,1 : 'sub_path'
                          ,2 : 'tertiary_path'})
    logs = logs.drop(columns='path')
    for x in [1,2,3]:
        print(f'List of most visited for Program {x}:')
        print()
        print(logs[logs.program_id == x][['main_path', 'sub_path']].value_counts().head())
        print('---------------------')

################ QUESTION 2 ####################

def zealous_cohorts(logs):
    '''Takes in the logs dataframe, splits the filepaths into main and sub-categories, calculated the Q1 and Q3 for number of visits to
    each filepath, and returns a dataframe with cohorts that visited that path significantly more than any other cohort ("significantly" 
    in this instances beind cohorts visiting more than IQR*3 above the "norm".)'''

    #Splitting file paths
    path_df = logs.path.str.split('/', 2, expand=True)
    logs = pd.concat([logs, path_df], axis = 1)
    logs = logs.rename(columns = {0 : 'main_path'
                          ,1 : 'sub_path'
                          ,2 : 'tertiary_path'})
    logs = logs.drop(columns='path')

    #Getting count for number of visits per cohort per page, their Q1 & Q3, and upper fence.

    visits = pd.DataFrame(logs[['main_path', 'sub_path', 'cohort_id']].value_counts().rename('num_visits'))
    visits = visits.reset_index().set_index(['main_path', 'sub_path'])
    visits = visits.merge(visits.groupby(['main_path', 'sub_path']).num_visits.quantile(.25), on=['main_path', 'sub_path'])
    visits = visits.merge(visits.groupby(['main_path', 'sub_path']).num_visits_x.quantile(.75), on=['main_path', 'sub_path'])
    visits = visits.rename(columns={'num_visits_x_x': 'num_visits'
                                ,'num_visits_y' : 'q1'
                                ,'num_visits_x_y': 'q3'})
    visits['upper_fence'] = visits.q3 + ( 3 * (visits.q3 - visits.q1))

    #Returns DF of cohorts that were beyond that upper range.

    return visits[visits.num_visits > visits.upper_fence].sort_values('cohort_id')

#------------------------------------------------

def zealous_cohorts_viz(visits):
    '''Taking in the visits df from the function zealous_cohorts, provides two bar charts depicting the top 3 "zealous" cohorts, and the 
    top 3 lessons that needed extra attention.'''

    plt.figure(figsize=(15,6))
    
    plt.subplot(1,2,1)
    visits[visits.num_visits > visits.upper_fence].cohort_id.value_counts().head(3).plot.bar()
    plt.title('Top 3 Visiting Cohorts')
    
    plt.subplot(1,2,2)
    visits[visits.num_visits > visits.upper_fence].index.value_counts().head(3).plot.bar()
    plt.title('Top 3 Overly-Visited Websites')
    plt.xticks(rotation=15)
    plt.show()

################ QUESTION 3 ####################

################ QUESTION 4 ####################

################ QUESTION 5 ####################

################ QUESTION 6 ####################

def lessons_after_grad(logs, program_id):
    '''Takes in the logs DF as well as a program ID number, splits filepath into main and sub-categories, and returns the top three lessons
    that cohorts visit after they have graduated from Codeup.'''

    #Splitting paths
    path_df = logs.path.str.split('/', 2, expand=True)
    logs = pd.concat([logs, path_df], axis = 1)
    logs = logs.rename(columns = {0 : 'main_path'
                          ,1 : 'sub_path'
                          ,2 : 'tertiary_path'})
    logs = logs.drop(columns='path')

    #Return function filtering out anything accessed before their graduation date.

    return logs[(logs.index > logs.end_date) & (logs.program_id == program_id)]\
                        .groupby(['main_path', 'sub_path'])[['user_id']].count().sort_values('user_id', ascending=False).head(3)

################ QUESTION 7 ####################

def least_accessed_ds(df):
    '''
    Input: df
    Action: creates new df, gets lessons from created file1 column, iterates over each lesson to get
    count of all lessons and returns the least number of lessons.
    Output: Bottom five least access lessons 
    '''
    # makes new df
    df1 = df.copy()
    # creates new columns
    df1[['folder', 'file1', 'file2']] = df1['path'].str.split('/', 2, expand=True)
    # isolates each lesson
    lessons = df1 [df1.file1.notnull()]
    # gets lesson counts
    lesson_counts = lessons.folder.value_counts()
    # creates df for ds students
    ds = lessons[(lessons.program_id == 3)].folder.value_counts()
    # dictionary for lesson counts
    combined_counts3 = {}
    # for loop to iterate over each lesson to count
    for lesson, count in ds.items():
        lesson_name = lesson.split('-')[-1]
        if lesson_name in combined_counts3:
            combined_counts3[lesson_name] += count
        else:
            combined_counts3[lesson_name] = count
    # sorting lessons from least to greatest lesson count
    least_accessed_lessons = sorted(combined_counts3.items(), key=lambda x: x[1])
    
    print("Lessons accessed the least:")
    for lesson, count in least_accessed_lessons:
        if 100 < count < 3500:
            print(f"{lesson}: {count}")

# ----------------------------------

def least_accessed_web_dev(df):
    '''
    Input: df
    Action: creates new df, gets lessons from created file1 column, iterates over each lesson to get
    count of all lessons and returns the least number of lessons.
    Output: least access lessons 
    '''
    # makes new df
    df1 = df.copy()
    # creates new columns
    df1[['folder', 'file1', 'file2']] = df1['path'].str.split('/', 2, expand=True)
    # isolates each lesson
    lessons = df1 [df1.file1.notnull()]
    # gets lesson counts
    lesson_counts = lessons.folder.value_counts()
    # creates df for web dev students
    web_dev = lessons[(lessons.program_id == 1) | (lessons.program_id == 2)].folder.value_counts().head(60)
    # dictionary for lesson counts
    combined_counts2 = {}
    # for loop to iterate over each lesson to count
    for lesson, count in web_dev.items():
        lesson_name = lesson.split('-')[-1]
        if lesson_name in combined_counts2:
            combined_counts2[lesson_name] += count
        else:
            combined_counts2[lesson_name] = count
    # sorting lessons from least to greatest lesson count
    least_accessed_lessons = sorted(combined_counts2.items(), key=lambda x: x[1])
    
    print("Lessons accessed the least:")
    for lesson, count in least_accessed_lessons:
        if 900 < count < 10000:
            print(f"{lesson}: {count}")














