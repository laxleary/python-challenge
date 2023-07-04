import os
import csv


#create variables, lists and dictionaries to store data
county = []
candidates = []
vote_counts = {}
total_votes = 0
vote_percentages = {}
winner = str()
percents = []

#open and read the csv file for our basic information
csvpath = os.path.join("PyPoll","Resources","election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader= next(csvreader)

    #Find the list of candidates
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
        #Count the total number of votes while looping through the rows
        total_votes +=1

    #Create a dictionary for each candidate's vote count
    for candidate in candidates: 
        vote_counts[candidate]=int(0)
        #Must re-open the file, as it will not read from the above
        with open(csvpath) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            
            #The csvheader line below may be unecessary due to the if statement
            
            for row in csvreader:
                if row[2] == candidate:
                    vote_counts[candidate]+=1 
            vote_percentages[candidate] = f"{round(vote_counts[candidate]/total_votes*100,3)}%"
            percents.append(round(vote_counts[candidate]/total_votes*100,3))
            
    for candidate in candidates:
        if vote_percentages[candidate] == f"{max(percents)}%":
            winner = candidate
        
    
#Create the txt file and specify where we would like it to be stored
output_path = os.path.join("PyPoll", "Analysis", "election_results.txt")

#Write the txt file
with open(output_path, 'w') as txtfile:
    txtfile.write(f" \n Election Results \n ----------------- \n Total Votes: {total_votes} \n -----------------")
    
with open(output_path, 'a') as txtfile:
    for candidate in candidates:
        txtfile.write(f"\n {candidate}: {vote_percentages[candidate]} ({vote_counts[candidate]})")
    txtfile.write(f"\n ----------------- \n Winner: {winner} \n ----------------- ")

with open(output_path, 'r') as txtfile:
    print(txtfile.read())