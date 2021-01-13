#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 13:02:18 2021

@author: jonnysheldon
"""

import os
import pandas as pd
from random import randint



term_dict = {
"names" : ["name","surname"],
"addresses" : ["address", "city", "country", "Postcode"],
"numbers" : ["NHS_number","phone_number", "Hospital_number"],
"date" : ["day","month","year"],
"tag_type" : ["clinician", "patient_other"]
    }

print(os.getcwd())
os.chdir("/home/jonnysheldon/Documents/MedCAT/dictionaries/")
print(os.getcwd())
## Read in the cvs files 
name_df = pd.read_csv("names.csv")
nhs = pd.read_csv("nhsNumber/nhs_numbers.txt",sep="\t")
address = pd.read_csv("addressSimulation.csv")

## functions

def year():
    year = []
    for i in range(0,180):
        i = i + 1841
        year.append(i)
    return year
    
    
def day():
    day = []
    for i in range(0,31):
        i = i + 1
        day.append(i)
    return day

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))

## Names ##
# get lists of personal terms 
name = name_df.name.tolist()
surdf = name_df[name_df['surnames'].notnull()]
surname = surdf.surnames.tolist()
#print(surname)

## NUmbers ##
# NHS numer
nhs_number = nhs.numbers.tolist()
#LANDLINE
landline = address["Phone number"].tolist()
just_landline  = [x.replace('(', '').replace(')', '') for x in landline]
#Modile
#Based on allowed charecters https://www.quora.com/What-is-the-format-for-mobile-numbers-in-the-UK

def mobile(amount_generated):
    mobile = []
    allowed_3rd_numbs = [1,2,3,4,5,7,8,9]
    per_choice = amount_generated / len(allowed_3rd_numbs)
    for i in range(0,len(allowed_3rd_numbs)):
        i = allowed_3rd_numbs[i]
        for j in range(0, int(per_choice)):
            k = '07' + str(i) + random_with_N_digits(9)
            mobile.append(k)
    return mobile

mob = mobile(2000)
#print(mob)

## addresses

address["city"] = address.Address.str.split(',').str[-1]
address["country"] = "UK"
address["Address"] = address.apply(lambda row : row['Address'].replace(str(row['city']), ''), axis=1)
print(address)

address_list = address["Address"].tolist()
city = address["city"].tolist()
country = address["country"].tolist()
postcode = address["Postcode"].tolist()

## Date

days = day()  
#print(days)  
month_numb = [1,2,3,4,5,6,7,8,9,10,11,12]
month_text = ["January","February","March","April","May","June","July","August","September","October","Novemeber","December"]
month_short_text = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
years = year()
#print(years)

term_dict_egs = {
"names" : [name,surname],
"addresses" : [address_list, city, country, postcode],
"numbers" : [nhs_number,landline, mob],
"date" : [day,month_numb, month_text, month_short_text,year],
"tag_type" : ["clinician", "patient_other"]
    }

print(term_dict_egs)