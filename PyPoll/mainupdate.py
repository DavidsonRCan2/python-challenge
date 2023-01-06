import csv
import numpy as np
import pandas as pd
import os

ballot = []
candidate = []


with open("Resources/election_data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)

    
    for row in reader:
        # row = [Ballot ID, County, Candidate]
        ballot.append(str(row["Ballot ID"]))
        candidate.append(str(row["Candidate"]))

    print(len(ballot))

    set_res = set(candidate)
    list_res = (list(set_res))

    for item in list_res:
        print(item)




