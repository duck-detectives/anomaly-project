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








def least_accessed_web_dev(df):
    '''
    Input: df
    Output: least access lessons 
    '''
    
    df1 = df.copy()
    df1[['folder', 'file1', 'file2']] = df1['path'].str.split('/', 2, expand=True)
    lessons = df1 [df1.file1.notnull()]
    lesson_counts = lessons.folder.value_counts()
    web_dev = lessons[(lessons.program_id == 1) | (lessons.program_id == 2)].folder.value_counts().head(60)
    
    combined_counts2 = {}
    
    for lesson, count in web_dev.items():
        lesson_name = lesson.split('-')[-1]
        if lesson_name in combined_counts2:
            combined_counts2[lesson_name] += count
        else:
            combined_counts2[lesson_name] = count
    
    least_accessed_lessons = sorted(combined_counts2.items(), key=lambda x: x[1])
    
    print("Lessons accessed the least:")
    for lesson, count in least_accessed_lessons:
        if 900 < count < 3500:
            print(f"{lesson}: {count}")




def least_accessed_ds(df):
    '''
    Input: df
    Output: Bottom five least access lessons 
    '''
    
    df1 = df.copy()
    df1[['folder', 'file1', 'file2']] = df1['path'].str.split('/', 2, expand=True)
    lessons = df1 [df1.file1.notnull()]
    lesson_counts = lessons.folder.value_counts()
    ds = lessons[(lessons.program_id == 3)].folder.value_counts()
    
    combined_counts3 = {}
    
    for lesson, count in ds.items():
        lesson_name = lesson.split('-')[-1]
        if lesson_name in combined_counts3:
            combined_counts3[lesson_name] += count
        else:
            combined_counts3[lesson_name] = count
    
    least_accessed_lessons = sorted(combined_counts3.items(), key=lambda x: x[1])
    
    print("Lessons accessed the least:")
    for lesson, count in least_accessed_lessons:
        if 100 < count < 3500:
            print(f"{lesson}: {count}")

















