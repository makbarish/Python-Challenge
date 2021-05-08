# In this challenge, we are helping a small, rural town modernize its vote counting process.

import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

count=0
candidate_list=[]
each_candidate=[]
voting_count=[]
voting_percentage=[]

with open (csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header =next(csvreader)
    for row in csvreader:
        count=count+1
        candidate_list.append(row[2])
    for i in set(candidate_list):
        each_candidate.append(i)
        j=candidate_list.count(i)
        voting_count.append(j)
        k=round((j/count)*100, 3)
        voting_percentage.append(k)
    winning_electionMax=max(voting_count)
    winner_election = each_candidate[voting_count.index(winning_electionMax)]


print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(each_candidate)):
    print(each_candidate[i] + ": " + str(voting_percentage[i]) +"% (" + str(voting_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner_election)
print("-------------------------")

with open('analysis.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(each_candidate))):
        text.write(each_candidate[i] + ": " + str(voting_percentage[i]) +"% (" + str(voting_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner_election + "\n")
    text.write("---------------------------------------\n")