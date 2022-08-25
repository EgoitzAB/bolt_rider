#!usr/bin python3
import requests
import pandas as pd

import csv
import tabula

from datetime import date, datetime

#Rentability and cost of the electro scooter delivery. The consumption cost
#ecuation is consumption = capacity x volt, divided under 1 millon to convert to KW,
#convert to KWh and multiplicate per load cost. After give delivery orders and
#multiplicate for the price of each order on the day. All saved two times, one in
#company pdf, other one saving price in month, and the benefits in other file,
#working in csv and pdf like exercise.

#download the pdf file to the computer using requests library and open method
#return the file in binary mode to extract the prices from pdf when is necessary

def download_get_pdf(url):
    download = requests.get(url)
    with download as r:
        with open("electricity.pdf", "wb") as f:
            f.write(r.content)
    print(f.name)
    return f.name

#reading the pdf file and extracting the actual price with pandas
def update_tariff(file):
    table = tabula.read_pdf(file, pages="all") #could improve extracting only first page
    df = pd.DataFrame(table[1]) #using panda extract first table
    actual_price = (df['Unnamed: 1'].loc[43]) #extract only my tariff_price
    format_price = actual_price.replace('(','').replace(')', '')\
    .replace(' ', '').replace(',','.') #format, could use regex but done
    tariff_price = float(format_price)
    return tariff_price #formated tariff_price for later processing
#tariff price during the months and save in csv, it could serve for other matters
def save_prices(price):
    price_dict = []
    currentMonth = datetime.now().strftime("%B") #get month
    current_prices = (currentMonth, price) # make tuple with month and price
    with open ('electricity_prices.csv', "a", newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(current_prices) #write the pair month price in csv to
#study later in a chart with mathpotlib
#function who calculate the load cost
def load_cost():
    with open('electricity_prices.csv', "r") as file:
        data = file.readlines()[-1]#get only the last input
        datos = data.split(',')[-1]#get only the price
    electricity_price = float(datos) / 1000 #format the price
    load_cost = electricity_price * load_capacity * load_time
    print(load_cost)
    cost_or_profit(load_cost)
#function who contains the option to output between cost or profit calculation
def cost_or_profit(load):
    question = input("Do you want to calculate the benefits? (y/n)")
    if question.lower() == "y":#option for profit calculation
        return profit(load)
    elif question.lower() == "n":#if not, save the cost and print
        with open("benefit.csv", "w+", encoding='UTF8') as f:
            writer = csv.writer(f, delimiter=' ')
            writer.writerow("The load cost is:{}".format(str(load)))
        return ("The load cost is: {}".format(str(load)))
    else:
        print("Choose the correct option, with the given format please.")
        cost_or_profit()

#fucntion who calculate the total profits of the day
def profit(load_cost):
    print(load_cost)
    order = int(input(">>How many orders do you make today?"))
    order_payment = int(input(">>How much is this week the order incomme?"))
    profit = order * order_payment #get the aprox. incomme
    benefit = profit - load_cost # sustract the cost and return benefit
    return benefit

#ONLY MAKE A TESTS, EXECUTABLE AND GITHUB
# give the variables in local scope for testing, and make one conditional to run
# update the first of the month
if __name__=='__main__':
    url = "https://www.pre.cz/Files/households/electricity/documents-for-download/price-lists/pre-proud-standard-predi/"
    load_time = 5.5
    load_capacity = (7650*36)/1000000 #batery capacity * volt / per one millon
    if date.today().day == 1: #call only first of month to update growing prices
        file = download_get_pdf(url)
        month_price = update_tariff(file)
        save_prices(month_price)
        load_cost()
    else:
        print(load_cost())
