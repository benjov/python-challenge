#
# PyPoll
#
#***********************************************************************
#   Analyzing vote-counting process in a small, rural town
#   DATA: election_data.csv
#   The dataset is composed of three columns: Voter ID, County, and Candidate
#***********************************************************************
# 
# Analysis of the votes and calculates each of the following:
# 
# 1. The total number of votes
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# 6. Print the analysis to the terminal and export a text file with the results

# I. Importing libraries:
import os
import csv

# II. Path to collect DATA:
election_data_csv = os.path.join('..', '..', 'python-challenge-DATA', 'election_data.csv')

# III. Function(s):
# III. Function(s):
def PyPoll(Dataset, Candidates):
    
    # Votes each candidate won
    Results = []
    Total_Votes = 0
    for candidate in Candidates:
        votes = 0
        for row in Dataset:           
            if row == candidate:
                votes = votes + 1
                Total_Votes = Total_Votes + 1
        Results.append([candidate, votes])
   
    Results = [row + [round(100*int(row[1])/Total_Votes, 3)] for row in Results]
#    print(Results)
#    print(Total_Votes)
    #
    Votes = []
    for row in Results:
        Votes.append(row[1])
    max_voted = max(Votes)
    #
    Cand = []
    for row in Results:
        Cand.append(row[0])
    #
    i = 0
    for vote in Votes:
        i = i + 1
        if vote == max_voted:
            break
    Winner = Cand[i-1]
 #   print(Winner)
    
    # Print out the Election Results
    print("*************************************************************")
    print("                 Election Results")
    print("*************************************************************")
    print(f"Total Votes: {Total_Votes}")
    print("*************************************************************")
    print(f"{Results[0][0]}: {Results[0][1]} ({Results[0][2]}%)")
    print(f"{Results[1][0]}: {Results[1][1]} ({Results[1][2]}%)")
    print(f"{Results[2][0]}: {Results[2][1]} ({Results[2][2]}%)")
    print(f"{Results[3][0]}: {Results[3][1]} ({Results[3][2]}%)")
    print("*************************************************************")
    print(f"Winner: {Winner}")
    print("*************************************************************")

    # Write CSV:
    election_results_csv = os.path.join('DATA', 'election_results.csv')
    with open(election_results_csv, 'w', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ',')
        csvwriter.writerow(['Variable', 'value', '%'])
        csvwriter.writerow(['Total Votes', Total_Votes, 100])
        csvwriter.writerow([Results[0][0], Results[0][1], Results[0][2]])
        csvwriter.writerow([Results[1][0], Results[1][1], Results[1][2]])
        csvwriter.writerow([Results[2][0], Results[2][1], Results[2][2]])
        csvwriter.writerow([Results[3][0], Results[3][1], Results[3][2]])

    # Write TXT:
    txtfile = open('DATA/election_results.txt', 'w')
    txtfile.write('************************************************************* \n') 
    txtfile.write('                 Election Results  \n')
    txtfile.write('*************************************************************  \n') 
    txtfile.write(f'{Results[0][0]}: {Results[0][1]} ({Results[0][2]}%)  \n')
    txtfile.write(f'{Results[1][0]}: {Results[1][1]} ({Results[1][2]}%)  \n')
    txtfile.write(f'{Results[2][0]}: {Results[2][1]} ({Results[2][2]}%)  \n')
    txtfile.write(f'{Results[3][0]}: {Results[3][1]} ({Results[3][2]}%)  \n')
    txtfile.write('*************************************************************  \n') 
    txtfile.write(f'Winner: {Winner} \n')
    txtfile.write('*************************************************************  \n') 
    txtfile.close() 

# IV: Reading and proccessing CSV file
with open(election_data_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
#    print(csvreader)
#    for row in csvreader:
#        print(row)
    
    header = next(csvreader)
#    print(f"CSV Header: {header}")

    # Create a list for Candidates:
    
    # List of all names not nunique:
    Candidates_rep = []
    for row in csvreader:
        Candidates_rep.append(row[2])
    
    # Select UNIQUE in teh list:
    Candidates = []
    for candidate in Candidates_rep:
        if candidate not in Candidates:
            Candidates.append(candidate)
#    print(Candidates)

    # Use the function:
    PyPoll(Candidates_rep, Candidates)

# END.