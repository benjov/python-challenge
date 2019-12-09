#
# PyBank
#
#***********************************************************************
#   Analyzing the financial records of some company 
#   DATA: budget_data.csv 
#   The dataset is composed of two columns: Date and Profit/Losses
#***********************************************************************
# 
# Analysis of the records to calculate each of the following:
# 
# 1. The total number of months included in the dataset
# 2. The net total amount of "Profit/Losses" over the entire period
# 3. The average of the changes in "Profit/Losses" over the entire period
# 4. The greatest increase in profits (date and amount) over the entire period
# 5. The greatest decrease in losses (date and amount) over the entire period
# 6. Printing the analysis to the terminal and export a text file with the results

# I. Importing libraries:
import os
import csv

# II. Path to collect DATA:
budget_data_csv = os.path.join('DATA', 'budget_data.csv')

# III. Function(s):
def PyBank(Dataset, Monthset):
    # The total number of months included in the dataset
    total_months = len(Monthset)

    # The net total amount of "Profit/Losses" over the entire period
    total_amount = sum(Dataset)

    # List of change in "Profit/Losses"
    Change = []
    for data in range(1, len(Dataset)):
        Change.append(Dataset[data] - Dataset[data-1])
        
    # The average of the changes in "Profit/Losses" over the entire period
    average_change = sum(Change)/len(Change)

    # The greatest increase in profits (date and amount) over the entire period
    max_change = max(Change)
    i = 0
    for change in Change:
        i = i + 1
        if change == max_change:
            break
    max_month = Monthset[i]

    # The greatest decrease in losses (date and amount) over the entire period
    min_change = min(Change)
    j = 0
    for change in Change:
        j = j + 1
        if change == min_change:
            break
    min_month = Monthset[j]
    
    # Print out the Financial Analysis
    print("*************************************************************")
    print("                 Financial Analysis")
    print("*************************************************************")
    print(f"Total number of months: {total_months}")
    print(f"Total amount of Profit/Losses: ${round(total_amount, 1)}")
    print(f"Average change in Profit/Losses: ${round(average_change, 2)}")
    print(f"Greatest increase in Profit/Losses: ${round(max_change, 1)}, ({max_month})")
    print(f"Greatest decrease in Profit/Losses: ${round(min_change, 1)}, ({min_month})")
    print("*************************************************************")

    # Write CSV:
    budget_results_csv = os.path.join('DATA', 'budget_results.csv')
    with open(budget_results_csv, 'w', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ',')
        csvwriter.writerow(['Variable', 'value'])
        csvwriter.writerow(['Total number of months', total_months])
        csvwriter.writerow(['Total amount of Profit/Losses', round(total_amount, 1)])
        csvwriter.writerow(['Average change in Profit/Losses', round(average_change, 2)])
        csvwriter.writerow(['Greatest increase in Profit/Losses', round(max_change, 1)])
        csvwriter.writerow(['Greatest increase in Profit/Losses (month)', max_month])
        csvwriter.writerow(['Greatest decrease in Profit/Losses', round(min_change, 1)])
        csvwriter.writerow(['Greatest decrease in Profit/Losses (month)', min_month])
    
    # Write TXT:
    txtfile = open('DATA/election_results.txt', 'w')
    txtfile.write('************************************************************* \n') 
    txtfile.write('                 Financial Analysis  \n')
    txtfile.write('*************************************************************  \n') 
    txtfile.write(f'Total number of months: {total_months}  \n')
    txtfile.write(f'Total amount of Profit/Losses: ${round(total_amount, 1)} \n')
    txtfile.write(f'Average change in Profit/Losses: ${round(average_change, 2)} \n')
    txtfile.write(f'Greatest increase in Profit/Losses: ${round(max_change, 1)}, ({max_month}) \n')
    txtfile.write(f'Greatest decrease in Profit/Losses: ${round(min_change, 1)}, ({min_month}) \n')
    txtfile.write('*************************************************************  \n') 
    txtfile.close() 


# IV: Reading and proccessing CSV file
with open(budget_data_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
#    print(csvreader)
#    for row in csvreader:
#        print(row)
    
    header = next(csvreader)
#    print(f"CSV Header: {header}")

    # Create a list for Datasets:
    ProfitLosses = []
    Months = []

    for row in csvreader:
        ProfitLosses.append(float(row[1]))
        Months.append(row[0])
        
    PyBank(ProfitLosses, Months)

# END.