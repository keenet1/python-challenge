#import os mudule and module for reading CSV files
import os
import csv
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")
file_to_save = os.path.join("PyPoll", "Analysis", "output_PyPoll.txt")

#create lists and/or dictionaries for candidates, percentage of votes won, & total vote counts
#declare variables to store
# initialize a total vote counter
total_vote_count = 0

#candidate names, vote percentage, and total vote counts
candidate_options = []
candidate_percentage = 0
candidate_votes = {}

#find and display the winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#print election results header
print("")
print("Election Results")
print("------------------------------")

#calculate and report the total votes
#special thanks to: https://github.com/antongit505/Election_Analysis/tree/main
with open (csvpath) as election_data:
    csvreader = csv.reader(election_data, delimiter=',')
    csv_header = next(csvreader)

    no_lines = len(list(csvreader))
    total_votes = (
        f"Total Votes: {no_lines}" + "\n"
        "------------------------------" + "\n")
    print(total_votes, end="")

with open(csvpath) as election_data:
    csvreader = csv.reader(election_data, delimiter=',')
    csv_header = next(csvreader)
       
    #create a for loop to count the votes for each candidate
    for row in csvreader:
        #add to the total vote count
        total_vote_count = total_vote_count + 1

        #get the candidate(s) name from each row
        candidate_name = row[2]

        #Get list of all unique candidate names(candidate options)
        if candidate_name not in candidate_options:
            #then, add the new name to the list
            candidate_options.append(candidate_name)
            #and also start counting their votes
            candidate_votes[candidate_name] = 0

        #add a vote to the candidates vote count total
        candidate_votes[candidate_name] +=1

    #show candidates, vote percentage, and total vote count
    for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_vote_count) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.3F}% ({votes})\n" )

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    
        print(f"{candidate_name}: {vote_percentage:.3F}% ({votes})")

    print("------------------------------")
    print((f"Winner: {winning_candidate}"))
    print("------------------------------")
    print("")

#Export a text file with the results
with open(file_to_save, "w") as txt_file:
    Poll_results = (
        "" + "\n"
        "Election Results" + "\n"
        "------------------------------" + "\n"
        f"Total Votes: {no_lines}" + "\n"
        "------------------------------" + "\n"
        f"{candidate_name}: {vote_percentage:.3F}% ({votes})" + "\n"
        "------------------------------" + "\n"
        f"Winner: {winning_candidate}" + "\n"
        "------------------------------" + "\n"
        "" + "\n")
    
    txt_file.write(Poll_results)

    
    
