import csv
import os

# File paths
input_file = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("analysis", "election_results.txt")

# Initialize variables
total_votes = 0
candidate_votes = {}
candidates = []
winner = ""
winner_votes = 0

# Read and analyze the dataset
with open(input_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    for row in csvreader:
        voter_id = row[0]
        candidate = row[2]

        # Count total votes
        total_votes += 1

        # Count votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
            candidates.append(candidate)

# Analyze the results
result_summary = []
result_summary.append("Election Results")
result_summary.append("-------------------------")
result_summary.append(f"Total Votes: {total_votes}")
result_summary.append("-------------------------")

# Calculate and display the percentage of votes each candidate won
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    result_summary.append(f"{candidate}: {percentage:.3f}% ({votes})")

    # Determine the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

result_summary.append("-------------------------")
result_summary.append(f"Winner: {winner}")
result_summary.append("-------------------------")

# Print the analysis to the terminal
for line in result_summary:
    print(line)

# Export the results to a text file
with open(output_file, "w") as txtfile:
    for line in result_summary:
        txtfile.write(line + "\n")
