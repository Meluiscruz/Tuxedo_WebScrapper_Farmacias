# -*- coding: utf-8 -*-
import numpy as np
import ast
import pandas as pd
import pymysql.cursors
import json

#Functions

def string_to_list(string):             #This function pulls apart a character a character string into list components.
    list_result = list(string.split(";"))
    return list_result

#Treatment of data before insert to database (tuxedo_log)

row_drugstore_5 = string_to_list(GetVar('vector_5'))

if row_drugstore_5[4] == ' No se encontro dato':             
    price_as_number_5 = 'NULL'    #isnan()
else:
    price_as_number_5 = row_drugstore_5[4].replace("MXN","").replace("$","").replace(",",".")

SetVar('vector_5',row_drugstore_5)

# Connect to the database

connection = pymysql.connect(host = 'localhost',                          #The host is the computer where it is run.
                             user = 'admin',                              #The user name.
                             password = 'Evil_Corp_24810_!',              #I think that should be hidden...
                             db = 'tuxedo_db',                            #Name of schema
                             charset = 'utf8mb4',                         #Specify the charset.
                             cursorclass = pymysql.cursors.DictCursor)    #What is this?
keyword = "{keyword}"
drugstore_site = "{tux_5}"
product_title = row_drugstore_5[2]
product_desc = row_drugstore_5[3]
price = price_as_number_5 
date_and_time_starts = "{opening_search}"
date_and_time_ends = "{ending_search}"

try:
    with connection.cursor() as cursor: 
        sql = "INSERT INTO product_metadata (keyword, drugstore_site, product_title, product_desc, price,\
                 date_and_time_starts, date_and_time_ends) VALUES ('"+ keyword +"', '" + drugstore_site + "',\
                 '"+ product_title +"', '"+ product_desc +"','" + price + "', '"+ date_and_time_starts + "',\
                 '"+ date_and_time_ends + "')"
        cursor.execute(sql)
        connection.commit()                   
finally:
    connection.close()
