import csv
import numpy as np
import pandas as pd
import os

csvfile = 'Resources/election_data.csv'
# df = pd.read_csv(csvfile)

votes = []
candidates = []
percent_by_cand =[]
votes_by_cand = []

with open(csvfile, "r"):
    reader = csv.DictReader(csvfile)
    is_first_row = True   # flag variable

    for row in reader:
        votes.append(str(row["Ballot ID"]))
        candidates.append(str(row["Candidate"]))

    print(len(votes))
    print(candidates)



