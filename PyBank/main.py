
import os
import csv


#create lists to store data
date = []
profit_losses = []

#open and read the csv file
csvpath = os.path.join("PyBank","Resources","budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader= next(csvreader)

    for row in csvreader:

        date.append(row[0])

        profit_losses.append(int(row[1]))

changes = []

for x in range(85):
    changes.append(profit_losses[x+1]-profit_losses[x])
    

total_months= len(date)
Total = sum(profit_losses)
average_change = sum(changes)/len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)

for i in range(85):
    if changes[i]==max(changes):
        gi_name = date[i+1]
    elif changes[i]==min(changes):
        gd_name = date[i+1]


financial_analysis = f"Financial Analysis \n -------------- \n Total Months: {total_months} \n Total: ${Total} \n Average Change: ${average_change} \n Greatest Increase in Profits: {gi_name} (${greatest_increase}) \n Greatest Decrease in Profits: {gd_name} (${greatest_decrease})"
output_path = os.path.join("PyBank", "Analysis", "financial_analysis.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write(f"{financial_analysis}")
print(f"{financial_analysis}")

print("Success!")