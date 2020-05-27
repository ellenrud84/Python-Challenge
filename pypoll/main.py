#import dependencies
import os
import csv

#specify path
election_file= os.path.join("Resources","election_data.csv")

#open csv file
with open(election_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #store header
    csv_header= next(csvreader)

    #initiate empty list to store names
    #votes_dict={"name":[names], "votes":[votes]}
    names=[]
    votes={}
    total_votes =0
    percentages =[] 

#get list of names and total votes
    #iterate through list
    for row in csvreader:
        #add one to total votes
        total_votes+=1
        #check if candidate name is aleady in dictionary
        if row[2] not in names:
            names.append(row[2])

#initiate value for all names in dictionary
for name in names:
    votes[name]=0

#re-initiate iterator
with open(election_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #store header
    csv_header= next(csvreader)
    #for each row in csv reader,  
    for row in csvreader:
        #check which name in names list is in that row
        for name in (names):
            if row[2]==name:
                #and add one to that name's count in the dictionary
                votes[row[2]]= votes[row[2]]+1
 
# calculate percentage of votes each candidate won
for name in names:
    percent =format((votes[name]/total_votes*100), '.3f')
    percentages.append(percent)

#determine winner
winner = max(votes, key=votes.get)

summary =(f'```Text \nElection Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n{names[0]}: {percentages[0]}% ({votes[names[0]]})\n{names[1]}: {percentages[1]}% ({votes[names[1]]})\n{names[2]}: {percentages[2]}% ({votes[names[2]]})\n{names[3]}: {percentages[3]}% ({votes[names[3]]})\n-------------------------\nWinner: {winner}\n-------------------------\n```')
print(summary)

#export results: specify output path
output_path= os.path.join("analysis","pypoll_results.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write(summary)
    txtfile.close()