import csv

# Initialize variables
total_months = 0
total_profit_losses = 0
changes = []
previous_profit_losses = None
greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}


# Open and read the CSV file
with open(r'C:\Users\jwidc\Desktop\python-challenge\PyBank\Resources\budget_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through each row in the CSV
    for row in reader:
        date = row['Date']
        profit_losses = int(row['Profit/Losses'])
        
        # Increment total months and add to total profit/losses
        total_months += 1
        total_profit_losses += profit_losses
        
        # Calculate changes in profit/losses
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)
            
            # Check for greatest increase
            if change > greatest_increase['amount']:
                greatest_increase['amount'] = change
                greatest_increase['date'] = date
            
            # Check for greatest decrease
            if change < greatest_decrease['amount']:
                greatest_decrease['amount'] = change
                greatest_decrease['date'] = date
        
        previous_profit_losses = profit_losses

# Calculate average change
average_change = sum(changes) / len(changes) if changes else 0

# Prepare the analysis results
results = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})"
)

# Print the analysis to the terminal
print(results)

# Export the results to a text file
with open(r'C:\Users\jwidc\Desktop\python-challenge\PyBank\analysis\financial_analysis.txt', mode='w') as file:
    file.write(results)
