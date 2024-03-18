#!usr/bin python3
import pdb
import requests
import pandas as pd

import csv
import tabula
import re

from datetime import datetime

"""Rentability and cost of the electro scooter delivery. The consumption cost
ecuation is consumption = capacity x volt, divided under 1 millon to convert to
KW, convert to KWh and multiplicate per load cost. After give delivery orders and
multiplicate for the price of each order on the day. All saved two times, one in
company pdf, other one saving price in month, and the benefits in other file,
working in csv and pdf like exercise."""

def download_get_pdf():#make a request and get the pdf
    download = requests.get(url)
    return download

#save the pdf and return the name to read later
def save_pdf(pdf):
    with pdf as r:
        with open("electricity.pdf", "wb") as f:
            f.write(r.content)
    return f.name

#reading the pdf file and extracting the actual price with pandas
def get_tariff_price(file):
    table = tabula.read_pdf(file, pages="all")
    df = pd.DataFrame(table[1]) #using panda extract first table
    actual_price = (df['Unnamed: 1'].loc[43]) #extract only my tariff_price
    return actual_price
#format the price for better handling
def format_tariff_price(actual_price):
    format_price = re.sub('[() ]', '', actual_price).replace(',', '.')
    tariff_price = float(format_price)
    return tariff_price

#save the tariff_price in one csvfile to work later
def save_prices(price):
    currentMonth = datetime.now().strftime("%B") #get month
    current_prices = (currentMonth, price) # make tuple with month and price
    with open ('electricity_prices.csv', "a", newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(current_prices)

#function who calculate the load cost and return the price
def get_today_price():
    with open('electricity_prices.csv', "r") as file:
        data = file.readlines()[-1]#get only the last input
        datos = data.split(',')[-1]#get only the price
    return datos
#make operations to calculate the load cost

def get_load_cost(datos):
    electricity_price = float(datos) / 1000 #format the price
    load_cost = electricity_price * load_capacity * load_time
    return load_cost

#save the cost of load and return in a string formated
def save_cost_of_load(load_cost):
    with open("benefit.csv", "w+", encoding='UTF8') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow("The load cost is:{}".format(str(load_cost)))
        return ("The load cost is: {}".format(str(load_cost)))

#function who calculate the total profits of the day
def profit(load_cost, profit):
    benefit = profit - load_cost # sustract the cost and return benefit
    return benefit


url = "https://www.pre.cz/Files/households/electricity/documents-for-download/price-lists/pre-proud-standard-predi/"
load_time = 5.5
load_capacity = (7650*36)/1000000 #batery capacity * volt / per one millon
