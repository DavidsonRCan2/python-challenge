import csv
import numpy as np
import pandas as pd

# Create list for months and profit/losses.
months = []
profit_losses = []
change_profitlosses = []
change_months = []
# Appending to months[] list
with open('Resources/budget_data.csv', "r") as csvfile:
    reader = csv.DictReader(csvfile)
    is_first_row = True   # flag variable

    for row in reader:
        months.append(str(row["Date"]))
        current_profit = int(row["Profit/Losses"])
        profit_losses.append(current_profit)
        
        if is_first_row:
            is_first_row = False    
        else:
            change_months.append(row["Date"])
            current_change = current_profit - previous_profit
            change_profitlosses.append(current_change)
        # set up for next row 
        previous_profit = current_profit
    
    total_months = len(months)
    total_net = sum(profit_losses)
    average = str(round(sum(change_profitlosses)/len(change_months),2))
    maxprofit = max(change_profitlosses)
    minprofit = min(change_profitlosses)

print("Financial Analysis")
print("----------------------------")
print("Total months: ", total_months)
print(f"Total net profits: ${total_net}")
print(f"Average change: ${average}")
print(f"Greatest increase in profits:  ${maxprofit}")
print(f"Greatest decrease in profit:  ${minprofit}")



    
    





