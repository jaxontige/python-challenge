#import file
import os
import csv
budget_csv = os.path.join("Resources", "budget_data.csv")

#read file
with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    next(csv_reader)


#name variables
    months = 0
    total = 0
    prev_rev = 0
    rev_change_list = []
    month_change_list = []
    total_change = 0

#for loop to calculate months, revenue, total, and average
    for row in csv_reader:
        months = months + 1
        revenue = int(row[1])
        total = total + revenue
       
        if prev_rev != 0 :
            rev_change = revenue - prev_rev
            rev_change_list.append(rev_change)
            month_change_list.append(row[0])
            total_change = total_change + rev_change

        prev_rev = revenue
    average_change = total_change / (months - 1)

#print outputs
    print(f'Total number of months: {months}')
    print(f'Total profit/loss: ${total}')
    print(f'Total change: {total_change}')
    print(f'Average change: ${average_change:.2f}')



#find max and min revenue changes 
    max_inc = max(rev_change_list)
    max_inc_month = month_change_list[rev_change_list.index(max_inc)]

    print(f"Greatest Increase in Profits: {max_inc_month} (${max_inc})")

    max_dec = min(rev_change_list)
    max_dec_month = month_change_list[rev_change_list.index(max_dec)]

    print(f"Greatest Decrease in Profits: {max_dec_month} (${max_dec})")


#create txt file information
export = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {max_inc_month} (${max_inc})\n"
    f"Greatest Decrease in Profits: {max_dec_month} (${max_dec})\n")
print(export)

#open and write "export" to txt file in analysis folder
export_file = "./analysis/export.txt"
with open(export_file, "w") as f:
    f.write(export)