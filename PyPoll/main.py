import csv
import pandas as pd

ballot = []
candidate = []

with open("Resources/election_data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        # row = [Ballot ID, County, Candidate]
        ballot.append(str(row["Ballot ID"]))
        candidate.append(str(row["Candidate"]))

    TotalVotes = len(ballot)
    
    # fo find individual candidate names
    # candidate_set = set(candidate)
    # candidate_list = list(candidate_set)
    # # print(candidate_list)

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
      
# print block texts
print(f"""Election Results
-----------------------------
Total Votes Cast: {TotalVotes}
-----------------------------""")
for i in range(len(count_df)):
    candidate_final = count_df.loc[i,"Candidate"]
    vote_final = count_df.loc[i, "Votes"]
    percent_final = '{:,.2%}'.format(vote_final/TotalVotes)
    print(f"{candidate_final}:  {percent_final}  ({vote_final})")
print(f"""-----------------------------
Winner: {winner}
-----------------------------
""")


# print out to text file
with open("/Users/rebeccadavidson/Library/CloudStorage/OneDrive-Personal/rice/Homework/03-python/python-challenge/PyPoll/Analysis/PyPoll_Output.txt", "w") as f:
    print(f"""Election Results
-----------------------------
Total Votes Cast: {TotalVotes}
-----------------------------""", file=f)
    for i in range(len(count_df)):
        candidate_final = count_df.loc[i,"Candidate"]
        vote_final = count_df.loc[i, "Votes"]
        percent_final = '{:,.2%}'.format(vote_final/TotalVotes)
        print(f"{candidate_final}:  {percent_final}  ({vote_final})", file=f)
    print(f"""-----------------------------
Winner: {winner}
-----------------------------
""", file=f)
f.close()
