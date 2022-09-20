import os
import csv


csvpath= os.path.join("Resources","election_data.csv")

all_votes = []
candidates = []
percent_votes = []
candidate_votes = []

with open(csvpath) as election:
    csvreader = csv.reader(election,delimiter=',')
    header = next(csvreader)
    # The total number of votes cast
    for row in csvreader:
        all_votes.append(row[0])
    # A complete list of candidates who received votes
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            candidate_votes.append(1)
        else:
            index = candidates.index(row[2])
            candidate_votes[index] += 1
    # The percentage of votes each candidate won
    #Define variable total_votes as an integer to be used to calculate % all_votes
    # (< all_votes is currently a list and cannot be used in a formula)
    total_votes = (len(all_votes))
    #iterate through candidate_votes
    for votes in candidate_votes:
        percent = (votes/total_votes)*100
        percent = "%.3f%%" %percent
        percent_votes.append(percent)
     
#The total number of votes each candidate won
winner = max(candidate_votes)
index = candidate_votes.index(winner)
winner_candidate = candidates[index]


# Outputs to text file
out_path = "pypoll.txt"
with open (out_path,"w") as f:
    f.write("Election Results\n\n")
    f.write("----------------------------\n")
    f.write(f"Total Votes: {len(all_votes)}\n")
    f.write("----------------------------\n")
    for i in range(len(candidates)):
        f.write(f"{candidates[i]}: {str(percent_votes[i])} ({str(candidate_votes[i])})\n")
    f.write("----------------------------\n")
    f.write(f"Winner: {winner_candidate}\n")
    f.write("----------------------------\n")
