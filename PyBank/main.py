
import os
import csv


#create lists to store data
date = []
profit_losses = []

#open and read the csv file (path is relative from inside of the PyBank folder, the location of this code file)
csvpath = os.path.join("Resources","budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #store the header as a variable
    csvheader= next(csvreader)

    #store lists of the date and profits/losses
    for row in csvreader:

        date.append(row[0])

        profit_losses.append(int(row[1]))

#calculate the relevant changes (in profits/losses)
changes = []

for x in range(85):
    changes.append(profit_losses[x+1]-profit_losses[x])
    
#collect values for the Financial Analysis
total_months= len(date)
Total = sum(profit_losses)
average_change = sum(changes)/len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)

#Collect the dates for the greatest increase/decrease information
for i in range(85):
    if changes[i]==max(changes):
        gi_name = date[i+1]
    elif changes[i]==min(changes):
        gd_name = date[i+1]

#Store our desired text as a variable
financial_analysis = f" \n Financial Analysis \n -------------- \n Total Months: {total_months} \n Total: ${Total} \n Average Change: ${average_change} \n Greatest Increase in Profits: {gi_name} (${greatest_increase}) \n Greatest Decrease in Profits: {gd_name} (${greatest_decrease}) \n"

#Create the txt file and specify where we would like it to be stored (path is relative from inside of the PyPoll folder, the location of this code file)
output_path = os.path.join("Analysis", "financial_analysis.txt")

#Write the txt file
with open(output_path, 'w') as txtfile:
    txtfile.write(f"{financial_analysis}")

#Also print to the terminal
print(f"{financial_analysis}")
