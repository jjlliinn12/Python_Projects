# Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#Import Modules
import os
import csv
# Read the csv file
csvpath = os.path.join(".","raw_data","election_data_2.csv")
#test filepath
print(csvpath)
#lists to store data

candidate = []

#open the csv and loop through rows to count votes
vote_count = 0
li_vote = 0
khan_vote = 0
correy_vote = 0
tooley_vote = 0
with open(csvpath, newline="") as csvfile:
    #skip the headers
    reader = csv.reader(csvfile)
    next(reader, None)
    csvreader = csv.reader(csvfile, delimiter=",")
    print("Election Results")
    print("-------------------------")
    # * The total number of votes cast
    for row in csvreader:
        vote_count = vote_count + 1
        #Add Candidate
        #Help: trying to sort through the list and add up all votes per candidate
        candidate.append(row[2])
    for candids in candidate:
        if candids == "Khan":
            khan_vote = khan_vote + 1
        elif candids == "Li":
            li_vote = li_vote + 1
        elif candids == "Correy":
            correy_vote = correy_vote + 1
        elif candids == "O'Tooley":
            tooley_vote = tooley_vote + 1



# totvot = khan_vote + li_vote + correy_vote + tooley_vote
# print(totvot)
#     
print("Total Votes: " + str(vote_count))
# this works too
# print(len(candidate))
print("-------------------------")
# * A complete list of candidates who received votes
# * The percentage of votes each candidate won
# * The total number of votes each candidate won
lipercent = round((li_vote/(vote_count)*100),1)
khanpercent = round((khan_vote/vote_count*100),1)
correypercent = round((correy_vote/vote_count*100),1)
tooleypercent = round((tooley_vote/vote_count*100),1)
print("Khan: " + str(khanpercent)  + "% " + "(" + str(khan_vote) + ")")
print("Li: " + str(lipercent) + "%" + "(" + str(li_vote) + ")")
print("Correy: " + str(correypercent) + "%" + "(" + str(correy_vote) + ")")
print("O'Tooley: " + str(tooleypercent) + "%" + "(" + str(tooley_vote) + ")")
print("-------------------------")

# * The winner of the election based on popular vote.
if (li_vote > khan_vote and li_vote > correy_vote and li_vote > tooley_vote):
    print("Winner: Li")
if (khan_vote > li_vote and khan_vote > correy_vote and khan_vote > tooley_vote):
    print("Winner: Khan")
if (correy_vote > khan_vote and correy_vote > li_vote and correy_vote > tooley_vote):
    print("Winner: Correy")
if(tooley_vote > khan_vote and tooley_vote > correy_vote and tooley_vote > li_vote):
    print("Winner: Tooley")
print("-------------------------")

# As an example, your analysis should look similar to the one below:

# ```
# Election Results
# -------------------------
# Total Votes: 620100
# -------------------------
# Rogers: 36.0% (223236)
# Gomez: 54.0% (334854)
# Brentwood: 4.0% (24804)
# Higgins: 6.0% (37206)
# -------------------------
# Winner: Gomez
# -------------------------

