#!usr/bin/python3
import argparse
from src.cost_and_benefit import viabilidad_reparto as v
from datetime import date



def main():
    if date.today().day == 1: #call only first of month to update growing prices
        file = v.download_get_pdf()
        pdf = v.save_pdf(file)
        get_tariff = v.get_tariff_price(pdf)
        formated = v.format_tariff_price(get_tariff)
        save_price = v.save_prices(formated)
        today_price = v.get_today_price()
        load_cost = v.get_load_cost(today_price)
        print(load_cost)
    elif date.today().day != 1:
        today_price = v.get_today_price()
        load_cost = v.get_load_cost(today_price)
        print(load_cost)
        return load_cost

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("orders", nargs='?', help="The number of today orders", type=int)
    parser.add_argument("payment", nargs='?', help="The week paymet of the orders", type=int)
    args = parser.parse_args()
    if args.orders and args.payment:
        answer = args.orders * args.payment
        today_price =v.get_today_price()
        load_cost = v.get_load_cost(today_price)
        benefit = v.profit(load_cost, answer)
        print(benefit)
    else:
        main()
