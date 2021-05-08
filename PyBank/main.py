import os
import csv

# Setting initial variables

total_number_months = 0
total_net_amount = 0
month_change = []
month_count = []
greatest_increase = 0
greatest_decrease = 0 
month_greatest_increase = 0
month_greatest_decrease = 0


# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')


# Opening and reading the Budget Data CSV file 
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter =',')

    #print(csvreader)

    # Reading the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    row = next(csvreader)
    #calculating the total number of months included in the dataset
    rowbefore = int (row [1])
    total_number_months = total_number_months + 1
    total_net_amount = total_net_amount + int (row[1])
    greatest_increase =  int (row[1])
    month_greatest_increase = row [0]
    #calculating the net total amount of "Profit/Losses" over the entire period
    for row in csvreader:

        total_number_months = total_number_months +1
        total_net_amount = total_net_amount + int (row[1])
        #calculating the average of the changes in "Profit/Losses" over the entire period

        #calculating the net profit/loss change 
        PL_change = int(row[1]) - rowbefore
        month_change.append (PL_change)
        rowbefore =int(row[1])
        month_count.append(row[0])




        # Calculate The Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            month_greatest_increase = row[0]
            
        # Calculate The Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            month_greatest_decrease = row[0]  
        

  # Calculating the average
# def average (numbers):
   
#     sum_numbers = 0

#     for i in numbers:
#         sum_numbers = sum_numbers + i
#         average = sum_numbers / len(numbers)

#     return average
#     #print("The average is ", average(numbers) )

    
    #average_change = sum(monthly_change)/ len(monthly_change)
    average_change = round (sum(month_change)/ len (month_change), 2)
    high = max(month_change)
    low = min(month_change)


# Printing results 
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_number_months}")
print(f"Total: ${total_net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {month_greatest_increase}, (${high})")
print(f"Greatest Decrease in Profits:, {month_greatest_decrease}, (${low})")

# Writing path for new text file as an output
output_file = os.path.join('analysis.txt')

# Opening the file as a text file
with open(output_file, 'w',) as txtfile:

# Writting/printing the updated data in new text file
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"-----------------------------\n")
    txtfile.write(f"Total Months: {total_number_months}\n")
    txtfile.write(f"Total: ${total_net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {month_greatest_increase}, (${high})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {month_greatest_decrease}, (${low})\n")