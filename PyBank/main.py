
import os
import csv

#create lists to store data
date = []
profit_losses = []

#open and read the csv file
csvpath = os.path.join(r"PyBank\Resources\budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader= next(csvreader)
    print(csvheader)

    for row in csvreader:

        date.append(row[0])

        profit_losses.append(row[1])


