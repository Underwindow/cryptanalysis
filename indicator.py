import csv
import pandas as pd
from stockstats import StockDataFrame

stock = StockDataFrame.retype(pd.read_csv('002032.csv'))

sma = [stock.get('close_5_sma')]
close = [stock.get('close')]

dates = []
closingPrices = []

with open('002032.csv', "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        dates.append(row[0])
        closingPrices.append(row[2])
print(dates)
print(closingPrices)

FILENAME = "Analysis.csv"

with open(FILENAME, "w", newline="") as file:
    columns = ["date", "Closing price", "MA"]
    writer = csv.writer(file)

