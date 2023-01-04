import csv

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

print("Sum: ", sum(profit_losses))
print(len(months))
print("Average is " , sum(change_profitlosses)/len(change_months))


    
    





