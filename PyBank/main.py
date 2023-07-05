import csv
import os

budget_csv_path = os.path.join("Budget_data", "budget_data.csv")
output_path = os.path.join("PyBank","analysis", "financial_analysis.txt")

total_months = 0
net_total = 0
previous_profit_loss = 0
change_list = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}
change = 0

with open(budget_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        total_months += 1
        current_profit_loss = int(row[1])
        net_total += current_profit_loss
        
        if total_months > 1:
            change = current_profit_loss - previous_profit_loss
            change_list.append(change)
            
        previous_profit_loss = current_profit_loss
        
        if change > greatest_increase["amount"]:
            greatest_increase["date"], greatest_increase["amount"] = row[0], change
        elif change < greatest_decrease["amount"]:
            greatest_decrease["date"], greatest_decrease["amount"] = row[0], change

average_change = sum(change_list) / len(change_list)

analysis_results = f"""\
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})
Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\
"""

print(analysis_results)

os.makedirs(output_path, exist_ok=True)

with open(output_path, "w") as output_file:
    output_file.write(analysis_results)
