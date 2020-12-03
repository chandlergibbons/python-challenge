import csv

#stores the csv data file location 
fileone = '/Users/Chibbbins/desktop/python-challenge/PyPoll/Resources/02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv'

# opens the file
with open(fileone) as f:
    #separates data and assigns the data set to a variable
    csvreader = csv.reader(f, delimiter=',')
    #all calc skips header
    csv_header = next(csvreader)
    
    #varlaible asignments for calculations
    vote_count = 0
    votes = 0
    candidates = []
    unique_list = []
    candidates_votes = []
    candidates_perc = []
    
    #counts total votes and adds the names of candidates 3rd row intex 2 to a new list called candidates
    for row in csvreader:
        vote_count += 1
        candidates.append(row[2])
    
    #takes list of candidates and creates a new list just including the unique values form the candidates list
    for x in candidates:
        if x not in unique_list: 
            unique_list.append(x)
    
    #iterates over each candidates name 
    for a in unique_list:
        #iterates over list containing colomn 3 keeping a tally of each instance of each name then appending totals to a new list then resetting the tally for the next name
        for b in candidates:
            if b == a:
                votes += 1
        candidates_votes.append(votes)
        votes = 0
    #iterates through each candidates votes calculating the percent value for each candidate and appending it to a new list
    for c in candidates_votes:
        candidates_perc.append(c / vote_count * 100)
    
    #finds the most votes
    max_vote = max(candidates_votes)
    
    #locates the index of the most votes
    winner_index = candidates_votes.index(max_vote)
    
    #assigns the winners name tot a variable based on the index from the previous calculation
    winner_name = (unique_list[winner_index]) 
            
#prints to terminal full analysis with formating            
print("Election Results\n---------------------------------\nTotal Votes: " + str(vote_count) + "\n---------------------------------\n" 
      + unique_list[0] + ": " + str("{:.3f}".format(candidates_perc[0])) + "% (" + str(candidates_votes[0]) + ")\n"
      + unique_list[1] + ": " + str("{:.3f}".format(candidates_perc[1])) + "% (" + str(candidates_votes[1]) + ")\n"
      + unique_list[2] + ": " + str("{:.3f}".format(candidates_perc[2])) + "% (" + str(candidates_votes[2]) + ")\n"
      + unique_list[3] + ": " + str("{:.3f}".format(candidates_perc[3])) + "% (" + str(candidates_votes[3]) + ")\n---------------------------------\nWinner: "
      + winner_name + "\n---------------------------------")

#stores a copy of the full analysis in a text file in the analysis folder
with open("/Users/Chibbbins/Desktop/python-challenge/PyPoll/Analysis/analysis.txt", "a") as f:
    
    print("Election Results\n---------------------------------\nTotal Votes: " + str(vote_count) + "\n---------------------------------\n" 
      + unique_list[0] + ": " + str("{:.3f}".format(candidates_perc[0])) + "% (" + str(candidates_votes[0]) + ")\n"
      + unique_list[1] + ": " + str("{:.3f}".format(candidates_perc[1])) + "% (" + str(candidates_votes[1]) + ")\n"
      + unique_list[2] + ": " + str("{:.3f}".format(candidates_perc[2])) + "% (" + str(candidates_votes[2]) + ")\n"
      + unique_list[3] + ": " + str("{:.3f}".format(candidates_perc[3])) + "% (" + str(candidates_votes[3]) + ")\n---------------------------------\nWinner: "
      + winner_name + "\n---------------------------------", file = f)
    


