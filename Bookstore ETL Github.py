# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 02:21:41 2025

This is an ETL pipeline that is built to simulate a bookstore that regularly
receives shipments of books. The records of each shipment are extracted from
the upload folder, cleaned, and loaded into a relational database.

@author: quire
"""

import pandas as pd
import numpy as np
import datetime as dt
import time
import sqlalchemy
import psycopg2

# Start Time
start = time.time()

""""""""""""""""""""""

EXTRACT

Extract the shipment order files from the upload folder.

"""""""""""""""""""""

# Extract the data from the shipment order file to a DataFrame
shipment = pd.read_csv("C:/*file path*/Python ETL Project - 6-12-25/shipment_order.csv")


""""""""""""""""""""""

TRANSFORM

Perform transformations and data quality checks on the data from the shipment
order.

"""""""""""""""""""""

def transformations(df):
    
    # Change date type of the order_date and shipment_date columns to date
    df['order_date'] = pd.to_datetime(df['order_date'], format="%m-%d-%Y")
    df['shipment_date'] = pd.to_datetime(df['shipment_date'], format="%m-%d-%Y")
    
    # Update the first_name and last_name columns to proper case
    df['first_name'] = df['first_name'].str.title()
    df['last_name'] = df['last_name'].str.title()
    
    # Change the quantity from decimal to integer
    df['quantity'] = df['quantity'].astype(int)
    
    # Change price to numeric
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    
    return df

transformations(shipment)

""""""""""""""""""""""

# DATA QUALITY CHECKS

Perform data quality checks after the transformations.

"""""""""""""""""""""


# UNIQUE ORDER ID CHECK
order_id_count = len(shipment['order_id'])
unique_id_check = shipment['order_id'].nunique() == order_id_count

if unique_id_check == True:
    _= input("\nUnique Order ID Check OK")
else:
    _= input("There are duplicate Order IDs. Please review.")

# BLANK ORDER ID CHECK
order_id_blank = shipment[shipment['order_id'].isnull()]
order_id_blank_count = len(order_id_blank)

if order_id_blank_count == 0:
    _= input("\nOrder ID Check OK")
else:
    print(order_id_blank)
    _= input(f"There are {order_id_blank_count} missing Order IDs. Please review.")


# UNIQUE BOOK ID CHECK
book_id_count = len(shipment['book_id'])
unique_id_check = shipment['book_id'].nunique() == book_id_count

if unique_id_check == True:
    _= input("\nUnique Book ID Check OK")
else:
    _= input("There are duplicate book IDs. Please review.")    
    
# BLANK BOOK ID CHECK
book_id_blank = shipment[shipment['book_id'].isnull()]
book_id_blank_count = len(book_id_blank)

if book_id_blank_count == 0:
    _= input("\nBook ID Check OK")
else:
    print(book_id_blank)
    _= input(f"There are {book_id_blank_count} missing Book IDs. Please review.")
    

# ORDER DATE BEFORE SHIPMENT DATE CHECK

date_check = shipment[['order_id', 'order_date', 'shipment_date']]

order_first = (shipment['order_date'] < shipment['shipment_date'])
shipment_first = (shipment['shipment_date'] < shipment['order_date'])

conditions = [order_first, shipment_first]
results = ['OK', 'Review']

date_check['date_check'] = np.select(conditions, results)
date_check_review = date_check[date_check['date_check'] == 'Review']

if len(date_check_review) == 0:
    _= input("\nDate Check OK")
else:
    _= input("There may be incorrect order and/or shipment dates. Please review.")
    

# STRING CHECKS IN PRICE AND QUANTITY

string_check = shipment[['order_id', 'title', 'price', 'quantity']]
string_check['price_check'] = string_check['price'].apply(lambda x: True
                                                          if isinstance(x, str)
                                                          else False)

string_check['quantity_check'] = string_check['quantity'].apply(lambda y: True
                                                          if isinstance(y, str)
                                                          else False)
price_string = True in string_check['price'].values
quantity_string = True in string_check['quantity'].values

if price_string == False:
    _= input("\nPrice Check OK")
else:
    _= input("The Price column contains a string. Please review.")
    

if quantity_string == False:
    _= input("\nQuantity Check OK")
else:
    _= input("The Quantity column contains a string. Please review.")
    
"""""""""""""""""

LOAD

"""""""""""""""""
# DATABASE CONNECTION

engine = sqlalchemy.create_engine(
    'postgresql+psycopg2://username:password@localhost:5432/database',
    echo=True
    )

shipment.to_sql('inventory', engine, if_exists='append', index=False, schema='bookstore')

now = dt.datetime.now()
shipment.to_csv("C:/*file path*/Python ETL Project - 6-12-25/Processed Orders/Orders/shipment_order " + 
                now.strftime("%m-%d-%Y %H%M%S") + ".csv", index=False)


""""""""""""""""""""""

DOCUMENTATION

Create a log file that summarizes the loaded data.

"""""""""""""""""""""


shipment_records = len(shipment)
total_books = sum(shipment['quantity'])
total_price = sum(shipment['price'])

log_file_path = ("C:/*file path*/Python ETL Project - 6-12-25/Processed Orders/Log Files/order_log " + 
                now.strftime("%m-%d-%Y %H%M%S") + ".txt")

with open(log_file_path, "w") as log:
    log.write(f"BOOKSTORE DATABASE UPDATE SUMMARY\n\nDate Completed: {now}\nRecords Added to Database: {shipment_records}\nTotal Books: {total_books}\nTotal Price: {total_price}")


""""""""""""""""""""""

RECORD TIME

"""""""""""""""""""""


end = time.time()
code_time = end - start

if code_time < 60:
    print(f"\nCode Execution Time: {round(code_time,2)} seconds")
else:
    print(f"\nCode Execution Time: {round(code_time / 60,2)} minutes")