import csv
import numpy as np
import pandas as pd
import os
import sys

ballot = []
candidate = []

with open("Resources/election_data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        # row = [Ballot ID, County, Candidate]
        ballot.append(str(row["Ballot ID"]))
        candidate.append(str(row["Candidate"]))

    TotalVotes = (len(ballot))
    
    # fo find individual candidate names
    set_res = set(candidate)
    list_res = (list(set_res))
    # print(list_res)

# to calculate how many votes per candidate
    count = pd.Series(candidate).value_counts()
    # print(count)

# set the above output to a dataframe with index and column names. 
# Then use df to calculate candidate percentage of votes
    count_df = pd.DataFrame(count).reset_index()
    count_df.columns = ["Candidate", "Votes"]
   
    # print(count_df)
    
    CandidateOutput = count_df["Candidate"].tolist()
    VoteOutput = count_df["Votes"].tolist()
    winningvotes = max(VoteOutput)
    winner = CandidateOutput[VoteOutput.index(winningvotes)]
    
print("Election Results")
print("-----------------------------")
print(f"Total Votes Cast: {TotalVotes}")
print("-----------------------------")
for i in range(len(count_df)):
    candidate_final = count_df.loc[i,"Candidate"]
    vote_final = count_df.loc[i, "Votes"]
    percent_final = '{:,.2%}'.format(vote_final/TotalVotes)
    print(f"{candidate_final}:  {percent_final}  ({vote_final})")
print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")

# print out to text file
with open("/Users/rebeccadavidson/Library/CloudStorage/OneDrive-Personal/rice/Homework/03-python/python-challenge/PyPoll/Analysis/PyPoll_Output.txt", "w") as f:
    print("Election Results", file=f)
    print("-----------------------------", file=f)
    print(f"Total Votes Cast: {TotalVotes}", file=f)
    print("-----------------------------", file=f)
    for i in range(len(count_df)):
        candidate_final = count_df.loc[i,"Candidate"]
        vote_final = count_df.loc[i, "Votes"]
        percent_final = '{:,.2%}'.format(vote_final/TotalVotes)
        print(f"{candidate_final}:  {percent_final}  ({vote_final})", file=f)
    print("-----------------------------", file=f)
    print(f"Winner: {winner}", file=f)
    print("-----------------------------", file=f)
f.close()
