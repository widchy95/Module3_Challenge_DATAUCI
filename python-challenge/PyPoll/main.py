import csv

# Initialize variables
total_votes = 0
candidate_votes = {}


# Open and read the CSV file
with open(r'C:\Users\jwidc\Desktop\python-challenge\PyPoll\Resources\election_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through each row in the CSV
    for row in reader:
        candidate = row['Candidate']
        total_votes += 1
        
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate vote percentages and find the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
with open(r'C:\Users\jwidc\Desktop\python-challenge\PyPoll\analysis\election_results.txt', mode='w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
