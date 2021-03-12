import pandas as pd
import csv
import os
import glob

dir_path = os.path.dirname(os.path.realpath(__file__))
# os.chdir(r"C:\Users\user\Desktop\files")
csv_files = glob.glob("*.csv")
print(csv_files)

df_list = []
for filename in sorted(csv_files):
    df_list.append(pd.read_csv(filename))
full_df = pd.concat(df_list)

full_df.to_csv('merged.csv', index=False)
print("CSVs merged successfully")


'''
further we can merge columns with datatype as date or can use

from dateutil import parser
s= 'Oct 1 2019'
parser.parse(s)

to parse all date fields in one scpecific format 

'''
