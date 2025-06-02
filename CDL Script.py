"""
Created on Thu Oct 24 17:20:20 2024
@author: squire


Description: This script for the monthly community development loan (CDL) process. It produces a list of the banks'
current CDLs to be included monthly report.

Previous Version: v7
Version Date: 5/30/25

Updates from previous version:
    - Data Quality Check: blank New/Renewal
    - Data Quality Check: blank Geography
    - Transformation: replace In/Out with Assessment Area/Regional/National
    - sort results by Bank then Action Date
    - Add "Innovative/ Flexible" to replace list
    - Status updates throughout code (5/16/25)
    - Boolean indexing for filters (5/30/25)
    - DQC: data format of Loan Amount (5/30/25)
    - Clean up Innovative/Flexible column (5/30/25)

FUTURE UPDATES:
    - 
    
"""

import pandas as pd
import datetime as dt
import time
from collections import defaultdict
import random
import numpy as np

# Record the start time
start_time = time.time()



"""

SETUP
    

"""
timestamp = dt.datetime.now().time()
print(f"\nIN PROGRESS: Setup - {timestamp}\n")


# Store series of dates to capture the reporting month and the preceding month for the file paths
first = dt.date.today().replace(day=1) # Reference to the first of the month
lm = first - dt.timedelta(days=1) # Reference to last month
pm = first - dt.timedelta(days=35) # Reference to the month before last month

# Create dictionaries with the bank acronyms and drop folder file paths.

cdl_files1 = {
             'bank3': "Z:filepath/" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank3 CDL Worksheet.xlsx",
             'bank4': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank4 CDL Worksheet.xlsx",
             'bank6': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank13 CDL Worksheet.xlsx",
             'bank8': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank8 CDL Worksheet.xlsx",
             'bank13': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank13 CDL Worksheet.xlsx"
             }

cdl_files2 = {
             'bank2': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank2 CDL Worksheet.xlsx",
             'bank7': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank7 CDL Worksheet.xlsx",
             'bank10': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank10 CDL Worksheet.xlsx",
             'bank14': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank14 CDL Worksheet.xlsx"
             }

cdl_files3 = {
             'bank1': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank1 CDL Worksheet.xlsx",
             'bank5': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank5 CDL Worksheet.xlsx",
             'bank9': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank9 CDL Worksheet.xlsx",
             'bank11': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank11 CDL Worksheet.xlsx",
             'bank12': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank12 CDL Worksheet.xlsx",
             'bank15': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank15 CDL Worksheet.xlsx"
             }

bank16_files = {
	'bank16_1': "Z:filepath" + lm.strftime("%Y") + "/" + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank16 CDLWS.xlsx",
             'bank16_2': "Z:filepath" + lm.strftime("%Y") + "/"  + lm.strftime("%#m") + ". " + lm.strftime("%B") +"bank16 CDLWS 2021-2024.xlsx"
	}


timestamp = dt.datetime.now().time()
print(f"Setup Complete - {timestamp}\n")

"""

EXCEL TO DATAFRAMES
    
    
Create DataFrames from each bank's CDL Excel file by naming the variable after
the key and reading the file path from the value of the dictionaries.

The headers for each file start on various rows and correspond with each dictionary group.

"""

timestamp = dt.datetime.now().time()
print(f"IN PROGRESS: DataFrame Creations - {timestamp}\n")

# Headers start on row 4 of the files in dict. group #1
for key, value in cdl_files1.items():
    exec(f"{key}=pd.read_excel({'value'},sheet_name='CDL WORKSHEET',header=3, usecols='A:X')")
   
# Headers start on row 5 of the files in dict. group #2
for key, value in cdl_files2.items():
    exec(f"{key}=pd.read_excel({'value'},sheet_name='CDL WORKSHEET',header=4, usecols='A:X')")

# Headers start on row 7 of the files in dict. group #3
for key, value in cdl_files3.items():
    exec(f"{key}=pd.read_excel({'value'},sheet_name='CDL WORKSHEET',header=6, usecols='A:X')")

# Headers start on row 2 of the files in bank16 dict.
for key, value in bank16_files.items():
    exec(f"{key}=pd.read_excel({'value'},sheet_name='CDL Worksheet',header=1, usecols='A:X')")


timestamp = dt.datetime.now().time()
print(f"DataFrame Creation Complete - {timestamp}\n")

"""

COMBINE FILES
    
Combining the DataFrames into one for transformations.
    
"""
timestamp = dt.datetime.now().time()
print(f"IN PROGRESS: Transformations - {timestamp}\n")

# Combine two bank16 CDL files


# Create list of the DataFrames
files = [bank1, bank2, bank3, bank4, bank5,
         bank6, bank16_1, bank16_2, bank7, bank8, bank9, bank10,
         bank11, bank12, bank13, bank14, bank15]

# Remane columns to remove extra spaces and ignore columns that don't apply
for df in files:
    df.rename(columns = {'New/ Renewal': 'New/Renewal',
                         'Innovative/ Flexible': 'Innovative/Flexible',
                         'Innovative Flexible': 'Innovative/Flexible',
                         'Innovative /Flexible': 'Innovative/Flexible',
                         'Organization/ Loan Name': 'Organization/Loan Name'}, inplace=True, errors='ignore')

# Filter each df to the data before the first blank row
for i, df in enumerate(files):
    first_blank_row = df.index[df.isnull().all(axis=1)].min()
    
    if not pd.isna(first_blank_row):
        files[i] = df.iloc[:first_blank_row]

# Combine each DataFrame into one single DataFrame
df = pd.concat(files)





"""

TRANSFORMATIONS
    
Complete transformations on the new combined DataFrame to clean the data.

 
"""


# Drop duplicates
df = df.drop_duplicates()

# Temp field rename for transformations
df.rename(
    columns={
        'Organization/Loan Name': 'Organization_Loan_Name',
        'Loan Amount': 'LoanAmount'
        },
    inplace=True
    )


# REMOVE NULL BANK AND ORGANIZATION
df = df[df['Bank'].notnull()]
df = df[df['Organization_Loan_Name'].notnull()]

# CONVERT ACTION DATE TO DATETIME AND REMOVE CDLS AFTER REPORTING MONTH
df['Action Date'] = df['Action Date'].apply(pd.to_datetime)
df = df[df['Action Date'] < first.strftime('%Y-%m-%d')]


# REMOVE LEADING AND TRAILING SPACES FROM BANK, STATE, AND GEOGRAPHY
df['Geography'] = df['Geography'].str.strip()
df['State'] = df['State'].str.strip()
df['Bank'] = df['Bank'].str.strip()

# Change fields back
df.rename(
        columns={
            'Organization_Loan_Name': 'Organization/Loan Name',
            'LoanAmount': 'Loan Amount'
            },
        inplace=True
        )
# bank8 transformation to remove old acronym
df['Bank'] = df['Bank'].replace('bank8_old', 'bank8')

# bank5 transformation to replace 'bank5' value with Lake Forest-IL AA value
df.loc[(df['Bank'] == 'bank5') & (df['State'] == 'IL'), 'Bank'] = 'bank5-area1'

# REPLACE IN/OUT WITH ASSESSMENT AREA/REGIONAL/NATIONAL

# Banks by state
il_banks = (
    'bank1', 'bank2', 'bank3', 'bank4', 'bank5-area1',
    'bank6', 'bank7', 'bank8', 'bank9-area1', 'bank10',
    'bank11-area1', 'bank11-area2', 'bank13', 'bank14', 'bank15'
    )
wi_banks = ('bank12-area1', 'bank12-area2', 'bank12-area3', 'bank12-area4', 'bank12-area5')
fl_banks = ('bank5-area2', 'bank5-area3')
mi_banks = ['bank16']

# Conditions for regional CDLs by state
il_out = (df['Bank'].isin(il_banks)) & (df['Geography'] == 'Out') & (df['State'] == 'IL')
wi_out = (df['Bank'].isin(wi_banks)) & (df['Geography'] == 'Out') & (df['State'] == 'WI')
fl_out = (df['Bank'].isin(fl_banks)) & (df['Geography'] == 'Out') & (df['State'] == 'FL')
mi_out = (df['Bank'].isin(mi_banks)) & (df['Geography'] == 'Out') & (df['State'] == 'MI')

# Removing any remaining "In" values from Geography
df['Geography'] = df['Geography'].replace('In', 'Assessment Area')

# Geography column conditions
geo_conditions = [
    df['Geography'] == "Assessment Area",
    df['Geography'] == "Regional",
    df['Geography'] == "National",
    il_out,
    wi_out,
    fl_out,
    mi_out
    ]

# Geography column values
geo_values = [
    'Assessment Area',
    'Regional',
    'National',
    'Regional',
    'Regional',
    'Regional',
    'Regional'
              ]

# Assign values to Geography column by mapping corresponding conditions
df['Geography'] = np.select(geo_conditions, geo_values, default='National')

# Sort CDLs by Bank and Action Date
df = df.sort_values(by=['Bank', 'Action Date'], ascending=[True, True])


timestamp = dt.datetime.now().time()
print(f"Transformations Complete - {timestamp}\n")

"""

DATA QUALITY CHECK: BLANK GEOGRAPHY

Checking for blank values in the Geography column.


"""

timestamp = dt.datetime.now().time()
print(f"IN PROGRESS: Data Quality Checks - {timestamp}\n")

blank_geo = df[df['Geography'].isnull()]
blank_geo = blank_geo[['Bank', 'Organization/Loan Name', 'Action Date', 'Geography']]

if len(blank_geo) == 0:
    print("\nGeography Check OK")
    _= input("\nPress any key to continue.")
else:
    blank_geo_count = len(blank_geo)
    print(f"\nThere are {blank_geo_count} rows with no Geography indicated.\n")
    print(blank_geo)
    _ = input("Please review.")


"""

DATA QUALITY CHECK: BLANK NEW/RENEWAL

Checking for blank values in the New/Renewal column.


"""

blank_nr = df[df['New/Renewal'].isnull()]
blank_nr = blank_nr[['Bank', 'Organization/Loan Name', 'Action Date', 'New/Renewal']]

if len(blank_nr) == 0:
    print("\nNew/Renewal Check OK")
    _= input("\nPress any key to continue.")
else:
    blank_nr_count = len(blank_nr)
    print(f"\nThere are {blank_nr_count} rows with no New/Renewal indicated.\n")
    print(blank_nr)
    _ = input("Please review.")
    


"""

DATA QUALITY CHECK: LOAN AMOUNT DATA TYPE

Checking the Loan Amount column for data that isn't an integer.


"""


loan_amount_str = df[df['Loan Amount'].apply(lambda x: isinstance(x, str))]
loan_amount_str = loan_amount_str[['Bank', 'Organization/Loan Name', 'Action Date', 'Loan Amount']]
if len(loan_amount_str) == 0:
    print("\nLoan Amount Check OK")
    _= input("\nPress any key to continue.")
else:
    loan_amount_str_count = len(loan_amount_str)
    print(f"\nThere are {loan_amount_str_count} rows with string Loan Amount values.\n")
    print(loan_amount_str)
    _ = input("Please review.")


"""

DATA QUALITY CHECK: BANK COLUMN VALUES

Checking the values to see if the correct AAs are entered in the Bank
column.

"""
# All possible Bank column values (AAs) in a set
bank_master = {
    'bank1', 'bank2', 'bank3', 'bank4', 'bank5-area1',
    'bank5-area2', 'bank5-area3', 'bank6', 'bank7', 'bank8',
    'bank9-area1', 'bank9-area2', 'bank10', 'bank11-area1', 'bank11-area2', 'bank12-area1',
    'bank12-area2', 'bank12-area3', 'bank12-area4', 'bank12-area5', 'bank13',
    'bank14', 'bank15', 'bank16'
            }

# Place all values within the Bank column in a list
bank_cdl = df['Bank'].tolist()

# Function to identify values that are foreign to bank_master and count the number of occurrences
def bank_check(cdl: list[str], master: set[str]):
    # default dict allows you to set a behavior for when you try to do something with a value not yet present in the dictionary
    # in this case we want to be able to increment the count without having to check first
    dq_values: dict[str, int] = defaultdict(int)
    for bank in cdl:
        if bank not in master:
            dq_values[bank] += 1
   
    if len(dq_values) == 0:
        print("\nBank Check OK")
        _= input("Press any key to continue...")
    else:
        print(dq_values) # incase there are many/multiple occurances of the same incorrect value get the count instead of the raw list
        
        # convention is to use an underscore when a function returns something but you don't need it
        _= input("Press any key to continue...")
        
bank_check(bank_cdl, bank_master)


"""

DATA QUALITY CHECK: EXAM PERIOD

Checking the Action Dates to see if the CDLs fall within the appropriate
exam periods.

"""
# Banks grouped by exam period
exam_2021 = 'bank16'
exam_2022 = ['bank4', 'bank9-area1', 'bank9-area2', 'bank12-area1','bank12-area2',
             'bank12-area3', 'bank12-area4', 'bank12-area5', 'bank13', 'bank14']
exam_2024 = ['bank1', 'bank2', 'bank5-area1','bank5-area2',
             'bank5-area3', 'bank8','bank10']
exam_2025 = ['bank3', 'bank6', 'bank7', 'bank11-area1', 'bank11-area2', 'bank15']


# Create a new DataFrame using the banks and their oldest and newest CDLs
dq_exam = df.groupby('Bank').agg({'Action Date':['min', 'max']}) #New DF
dq_exam.columns = ['Oldest', 'Newest'] # Flatten/rename columns
dq_exam = dq_exam.reset_index() # Reset index and move Bank to its own column

# CREATE CONDITIONS AND RESULTS TO DETERMINE IF CDLS ARE WITHIN BANKS' EXAM PERIODS

# Exam period conditions for the oldest CDLs
after_2020 = (dq_exam['Bank'] == exam_2021) & (dq_exam['Oldest'] > '2020-12-31')
before_2021 = (dq_exam['Bank'] == exam_2021) & (dq_exam['Oldest'] < '2021-01-01')
after_2021 = (dq_exam['Bank'].isin(exam_2022)) & (dq_exam['Oldest'] > '2021-12-31')
before_2022 = (dq_exam['Bank'].isin(exam_2022)) & (dq_exam['Oldest'] < '2022-01-01')
after_2023 = (dq_exam['Bank'].isin(exam_2024)) & (dq_exam['Oldest'] > '2023-12-31')
before_2024 = (dq_exam['Bank'].isin(exam_2024)) & (dq_exam['Oldest'] < '2024-01-01')
after_2024 = (dq_exam['Bank'].isin(exam_2025)) & (dq_exam['Oldest'] > '2024-12-31')
before_2025 = (dq_exam['Bank'].isin(exam_2025)) & (dq_exam['Oldest'] < '2025-01-01')

# Checking for CDLs that are too old for exam periods
conditions_old = [
    after_2020, before_2021,
    after_2021, before_2022,
    after_2023, before_2024,
    after_2024, before_2025
    ]
results_old = [
    'OK', 'Check',
    'OK', 'Check',
    'OK', 'Check',
    'OK', 'Check'
               ]

# Exam period conditions for the newest CDLs
before_the_first = (dq_exam['Newest'] < first.strftime('%Y-%m-%d'))
after_last_month = (dq_exam['Newest'] > lm.strftime('%Y-%m-%d'))

# Checking for CDLs that are beyond the reporting month
conditions_new = [before_the_first, after_last_month]

results_new = ['OK', 'Check']

# Create new columns based on the conditions
dq_exam['Old Check'] = np.select(conditions_old, results_old)
dq_exam['New Check'] = np.select(conditions_new, results_new)

# Create Series with CDLs to review
old_check = dq_exam['Old Check'] == 'Check'
new_check = dq_exam['New Check'] == 'Check'

# Check for CDLs that are too old for each bank's exam period
if dq_exam['Old Check'].str.contains('Check').any():
    print(dq_exam.loc[old_check,['Bank', 'Oldest', 'Old Check']])
    _= input("Press any key to continue.")
else:
    print(dq_exam[['Bank', 'Oldest', 'Old Check']])
    _= input("\nOld Check OK\nPress any key to continue.")
        
# Check for CDLs that are too new for each bank's exam period
if dq_exam['New Check'].str.contains('Check').any():
    print(dq_exam.loc[new_check,['Bank', 'Newest', 'New Check']])
    _= input("Press any key to continue.")
else:
    print(dq_exam[['Bank', 'Newest', 'New Check']])
    _= input("\nNew Check OK\nPress any key to continue")    


timestamp = dt.datetime.now().time()
print(f"Data Quality Checks Complete - {timestamp}\n")

"""

FINALIZE FILE

Read the final DataFrame to an Excel file to be uploaded to SharePoint.
    
"""

timestamp = dt.datetime.now().time()
print(f"IN PROGRESS: Final File - {timestamp}\n")

# # Store today's date to use for the final file name
now = dt.datetime.now()


# Create Excel writer object and write to Excel
file_path = ("Z:filepath" + lm.strftime("%Y") +"/"
             + lm.strftime("%#m") + ". " + lm.strftime("%B") +
             lm.strftime("%B %Y") +" CDLs Cleaned " + now.strftime("%m-%d-%y %I%M%S") + ".xlsx")

with pd.ExcelWriter(file_path, engine='xlsxwriter') as cdl_writer:
    df.to_excel(cdl_writer, index=False, sheet_name="Data")
    
    # Get the workbook and worksheet objects to update and save the Excel file
    workbook = cdl_writer.book
    worksheet = cdl_writer.sheets["Data"]
    
    # Get the numbers of rows and columns from the df
    (max_row, max_col) = df.shape
    
    # Random number for Excel table style
    random_int = random.randint(1, 7)

    # Put the Excel file data in an Excel table using the shape of the df
    worksheet.add_table(
        0, 0, max_row, max_col - 1, {
            "columns": [{"header": col} for col in df.columns],
            "style": f"Table Style Medium {random_int}",
            "name": "CDLs"
            }
        )
    # Set column width
    worksheet.set_column(0, max_col - 1, 20)




timestamp = dt.datetime.now().time()
print(f"Final File Complete - {timestamp}\n")


# Record the end time
end_time = time.time()

code_time = end_time - start_time

if code_time < 60:
    print(f"\nCode Execution Time: {round(code_time,2)} seconds")

else:
    print(f"\nCode Execution Time: {round((end_time - start_time) / 60,2)} minutes")