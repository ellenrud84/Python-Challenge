#import modules
import os
import csv
import pandas as pd 
import numpy as np 

#specify path
election_file= os.path.join("Resources","election_data.csv")

#open csv file
with open(election_file, 'r'):
    election_df = pd.read_csv(election_file)

#determine total number of votes cast
total_votes = len(election_df)

#determine list of candidates:
cand_list= election_df["Candidate"].unique()
print(cand_list)

#determine number of votes each candidate in cand_list got 
cand_ds = election_df["Candidate"]
cand_count = cand_ds.value_counts()
print(cand_count)

#detemine percent of overall votes each candidate got:
cand_percent= cand_ds.value_counts(normalize=True).mul(100).round(1).astype(str)+'%'

cand_percent_df = cand_percent.to_frame
winner = cand_percent.idxmax()
print(winner)
