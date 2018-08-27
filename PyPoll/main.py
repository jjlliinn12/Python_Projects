import csv
# * The total number of votes cast

# * A complete list of candidates who received votes

# * The percentage of votes each candidate won

# * The total number of votes each candidate won

# * The winner of the election based on popular vote

# Files to load and output (Remember to change these)
file_to_load = "raw_data/election_data_2.csv"
file_to_output = "analysis/election_analysis_2.txt"

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    #Each Row
    for row in reader: 

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row["Candidate"]

        #Add in new candidates as it reads each row
        if candidate_name not in candidate_options:

            #Append candidate name to list
            candidate_options.append(candidate_name)

            #Track candidate's vote count 
            candidate_votes[candidate_name] = 0

        #Add vote count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Print results
with open(file_to_output, "w") as txt_file:

    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")


    # Save the final vote count to the text file
    txt_file.write(election_results)

     # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate


         # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

            
