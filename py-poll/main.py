#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
#You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

#import csv
import os
import csv
poll_data = os.path.join("Resources", "election_data.csv")

#list variables
Candidates = {}
Names_List = []
Names_Set = set()
Total_Votes = 0

#read csv
with open(poll_data, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        if len(row) > 2:
            Total_Votes += 1
            Ballot_ID = row[0]
            County = row[1]
            Candidate = row[2]
            if Candidate not in Names_List:
                Names_List.append(Candidate)
                Candidates[Candidate] = 1
            else:
                Candidates[Candidate] += 1

# Calculate and display the percentage of votes for each candidate
for candidate, votes in Candidates.items():
    percentage = (votes / Total_Votes) * 100
    Candidates[candidate] = {
        'votes': votes,
        'percentage': percentage
    }

# Find the winner
winner = max(Candidates, key=lambda x: Candidates[x]['votes'])


# Prepare the full text with line breaks
val = "\n\n".join([f"{candidate}: {Candidates[candidate]['percentage']:.3f}% ({Candidates[candidate]['votes']})" for candidate in Names_List])
Output = f'''
Election Results
----------------------------
Total Votes: {Total_Votes}
----------------------------
{val}
----------------------------
Winner: {winner}
----------------------------
'''


# Print the full text
print(Output)


#open and write "export" to txt file in analysis folder
export_file = "./Analysis/Result.txt"
with open(export_file, 'w') as f:
    f.write(Output)