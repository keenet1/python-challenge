#import os mudule and module for reading CSV files
import os
import csv
csvpath = os.path.join('python-challenge', 'PyBank', 'Resources', 'budget_data.csv')


# Print Financial Anaysis Header
print("")
print("Financial Analysis")
print("------------------------------")

# Count the total number of months included in the dataset
with open(csvpath) as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')
    csv_header = next(csvreader)

    no_lines = len(list(csvreader))
    print(f"Total Months: {no_lines}")

 #Calculate the net total Profit/Loss amount
 #Special thanks to: https://stackoverflow.com/questions/65151369/summing-a-column-in-a-csv-file-using-python
with open(csvpath) as budget_data:
    data = csv.reader(budget_data, delimiter=',')
    total = 0
    for row in data:
        if not str(row[1]).startswith('P'):
            total = total + int(row[1])
    print(f"Total: ${total}")

#Calculate the average of the Profit/Loss changes
# Special tanks to: https://github.com/fnusandhiya/python-challenge/blob/master/Pybank/main.py
with open(csvpath) as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')
    csv_header = next(csvreader)

    months = []
    profits_losses = []


    for rows in csvreader:
        months.append(rows[0])
        profits_losses.append(int(rows[1]))

    revenue_change = []

    for x in range(1, len(profits_losses)):
        revenue_change.append((int(profits_losses[x]) - int(profits_losses[x-1])))

    revenue_average = sum(revenue_change) / len(revenue_change)
    rounded_revenue_average = round(revenue_average,2)
    print(f"Average Change: ${rounded_revenue_average}")

#Show the greatest increase in profits (date and amount)
    greatest_increase = max(revenue_change)
    print(f"Greatest Increase in Profits: {months[revenue_change.index(max(revenue_change))+1]} (${greatest_increase})")

#Show the greatest decrease in profits (dare and amount)
    greatest_decrease = min(revenue_change)
    print(f"Greatest Decrease in Profits: {months[revenue_change.index(min(revenue_change))+1]} (${greatest_decrease})")
    print("")

#Export a text file with the results
file = open("output_PyBank.txt", "w")
file.write("" + "\n")
file.write("Financial Analysis" + "\n")
file.write("------------------------------" + "\n")
file.write(f"Total Months: {no_lines}" + "\n")
file.write(f"Total: ${total}" + "\n")
file.write(f"Average Change: ${rounded_revenue_average}" + "\n")
file.write(f"Greatest Increase in Profits: {months[revenue_change.index(max(revenue_change))+1]} (${greatest_increase})" + "\n")
file.write(f"Greatest Decrease in Profits: {months[revenue_change.index(min(revenue_change))+1]} (${greatest_decrease})" + "\n")
file.write("" + "\n")
file.close()