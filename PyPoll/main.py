import csv
import os

csv_path = os.path.join("Resources" , "election_data.csv")
output_path = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidates = {}

with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  

    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        candidates[candidate] = candidates.get(candidate, 0) + 1

analysis_results = f"""\
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------\n"""

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    analysis_results += f"{candidate}: {percentage:.3f}% ({votes})\n"

winner = max(candidates, key=candidates.get)

analysis_results += f"""\
-------------------------
Winner: {winner}
-------------------------"""

print(analysis_results)

with open(output_path, "w") as output_file:
    output_file.write(analysis_results)
