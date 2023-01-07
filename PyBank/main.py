import csv
import numpy as np
import pandas as pd
import os

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
        
        # to skip first row since it is header
        if is_first_row:
            is_first_row = False    
        else:
            change_months.append(row["Date"])
            current_change = current_profit - previous_profit
            change_profitlosses.append(current_change)
        # set up for next row 
        previous_profit = current_profit
    
    # variables for easier printout
    total_months = len(months)
    total_net = sum(profit_losses)
    average = str(round(sum(change_profitlosses)/len(change_months),2))
    maxprofit = max(change_profitlosses)
    maxprofit_date = change_months[change_profitlosses.index(maxprofit)]
    minprofit = min(change_profitlosses)
    minprofit_date = change_months[change_profitlosses.index(minprofit)]

# print block texts
print(f"""Financial Analysis"
----------------------------
Total months: {total_months}
Total net profits: ${total_net}
Average change: ${average}
Greatest increase in profits:  ${maxprofit} on {maxprofit_date}
Greatest decrease in profit:  ${minprofit} on {minprofit_date}""")

# print out to text file
with open("/Users/rebeccadavidson/Library/CloudStorage/OneDrive-Personal/rice/Homework/03-python/python-challenge/PyBank/Analysis/PyBank_Output.txt", "w") as f:
    print(f"""Financial Analysis
----------------------------
Total months: {total_months}
Total net profits: ${total_net}
Average change: ${average}
Greatest increase in profits:  ${maxprofit} on {maxprofit_date}
Greatest decrease in profit:  ${minprofit} on {minprofit_date}""", file=f)
f.close()

    



    





    
    





