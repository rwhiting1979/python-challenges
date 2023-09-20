import csv
import os

# File paths
input_file = os.path.join("Resources","budget_data.csv")
output_file = os.path.join("analysis", "financial_analysis.txt")

# Initialize variables
total_months = 0
net_total = 0
previous_profit = 0
monthly_changes = []
dates = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# Read and analyze the dataset
with open(input_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])

        # Calculate the total number of months and net total
        total_months += 1
        net_total += profit_loss

        # Calculate the change in profit/loss compared to the previous month
        if total_months > 1:
            monthly_change = profit_loss - previous_profit
            monthly_changes.append(monthly_change)
            dates.append(date)

            # Check for the greatest increase and decrease
            if monthly_change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = monthly_change
            elif monthly_change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = monthly_change

        # Update the previous profit for the next iteration
        previous_profit = profit_loss

# Calculate the average change
average_change = sum(monthly_changes) / len(monthly_changes)

# Generate the financial analysis summary
financial_analysis = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})"
)

# Print the analysis to the terminal
print(financial_analysis)

# Export the results to a text file
with open(output_file, "w") as txtfile:
    txtfile.write(financial_analysis)
