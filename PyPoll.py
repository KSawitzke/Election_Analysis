# The data we need to retrieve
#    1. The total number of votes cast
#    2. A complete list of candidates who received votes
#    3. The percentage of votes each candidate won
#    4. The total number of votes each candidate won
#    5. The winner of the election based on popular vote

# Import dependancies
import csv
import os
from wsgiref.types import WSGIEnvironment

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# Create a filename variable to a direct or indirect path to the file. 
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Initialize vote counter, candidate options, candidate votes
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
# To do: perform analysis.
    # Read and print the header row.
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    # Determine the percentage of votes for each candidte by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculcate percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # To do: Print out each candidate's name, vote count, and percentage of votes.
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to terminal.
        print(candidate_results)
        # Save candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)