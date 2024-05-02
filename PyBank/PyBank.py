import os, csv

# Path to collect data from the Resources folder
csvpath = os.path.join('PyBank/Resources/budget_data.csv')

# Initiate variables in case there are no records in the file which will cause an error when trying to print the results
total_months = 0
total_profit = 0
prev_profit = 0
current_change = 0
total_change = 0
average_change = 0
greatest_increase_mth = ""
greatest_increase_amt = 0
greatest_decrease_mth = ""
greatest_decrease_amt = 0

# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first. If there is no header, set the header to None
    # Source for avoiding StopIteration error when csv file is blank: https://stackoverflow.com/questions/34470416/stopiteration-when-use-csv-in-python2 
    csv_header = next(csvreader, None)

    # Read each row of data after the header
    for row in csvreader:
        # Count the total number of months
        total_months += 1

        # Calculate the total profit by accumulating the profit/losses
        total_profit += int(row[1])

        # Calculate the change in profit/losses
        current_change = int(row[1]) - prev_profit

        # Skip the first profit/losses as there is no previous profit to compare
        if (total_months > 1):
          total_change += current_change

          # Check if the current change is the greatest increase. Store the month and amount if it is
          if (current_change > greatest_increase_amt):
              greatest_increase_mth = row[0]
              greatest_increase_amt = current_change

          # Check if the current change is the greatest decrease. Store the month and amount if it is
          if (current_change < greatest_decrease_amt):
              greatest_decrease_mth = row[0]
              greatest_decrease_amt = current_change

        # Store the current profit/losses to be used in the next iteration
        prev_profit = int(row[1])
        
    # Calculate the average change in profit/losses only if there are more than 1 month
    # Note: The average change is calculated by dividing the total change by the total number of months minus 1
    if (total_months > 1):
      average_change = total_change / (total_months - 1)
    else:
      average_change = 0

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profit: ${total_profit}")

    # Check if any analysis was done. If not, print a message to the file but display Total months and Total profit
    if (total_months <= 1):
      print("No data to analyze\n")
    else:
      print(f"Average Change: ${average_change:.2f}")
      print(f"Greatest Increase in Profits: {greatest_increase_mth} (${greatest_increase_amt})")
      print(f"Greatest Decrease in Profits: {greatest_decrease_mth} (${greatest_decrease_amt})")

# write the results to a text file
output_file = os.path.join("PyBank/Analysis/financial_analysis.txt")
with open(output_file, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")

    # Check if any analysis was done. If not, print a message to the file but display Total months and Total profit
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total Profit: ${total_profit}\n")
    if (total_months <= 1):
      textfile.write("No data to analyze\n")
    else:
      textfile.write(f"Average Change: ${average_change:.2f}\n")
      textfile.write(f"Greatest Increase in Profits: {greatest_increase_mth} (${greatest_increase_amt})\n")
      textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_mth} (${greatest_decrease_amt})\n")