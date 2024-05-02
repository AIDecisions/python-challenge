import os, csv

# Path to collect data from the Resources folder
csvpath = os.path.join('PyPoll/Resources/election_data.csv')

# Initiate variables in case there are no records in the file which will cause an error when trying to print the results  
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first. If there is no header, set the header to None
    # Source for avoiding StopIteration error when csv file is blank: https://stackoverflow.com/questions/34470416/stopiteration-when-use-csv-in-python2 
    csv_header = next(csvreader, None)

    # Read each row of data after the header
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1

        # Check if the candidate is already in the dictionary
        if row[2] in candidates:
            # Increment the candidate's vote count
            candidates[row[2]] += 1
        else:
            # Add the candidate to the dictionary
            candidates[row[2]] = 1

    # Print the election results
    print("Election Results")
    print("-------------------------")

    # Check if there are no votes. If there are no votes, print a message and exit the program
    if (total_votes == 0):
        print("There are no votes to count.")
    else:
        print(f"Total Votes: {total_votes}")
        print("-------------------------")

        # Loop through the candidates dictionary to print the results
        for candidate in candidates:
            # Calculate the percentage of votes for the candidate
            percentage = (candidates[candidate] / total_votes) * 100
            print(f"{candidate}: {percentage:.3f}% ({candidates[candidate]})")

            # Check if the candidate has the most votes so far
            if (candidates[candidate] > winner_votes):
                winner = candidate
                winner_votes = candidates[candidate]

        print("-------------------------")
        print(f"Winner: {winner}")
        print("-------------------------")

    # Write the results to a text file
    with open("PyPoll/analysis/election_results.txt", "w") as text_file:
        text_file.write("Election Results\n")
        text_file.write("-------------------------\n")

        # Check if there are no votes. If there are no votes, print a message and exit the program
        if total_votes == 0:
            text_file.write("There are no votes to count.\n")
        else:
            text_file.write(f"Total Votes: {total_votes}\n")
            text_file.write("-------------------------\n")

            # Loop through the candidates dictionary to print the results
            for candidate in candidates:
                # Calculate the percentage of votes for the candidate
                percentage = (candidates[candidate] / total_votes) * 100
                text_file.write(f"{candidate}: {percentage:.3f}% ({candidates[candidate]})\n")
                
            # Write the winner to the text file
            text_file.write("-------------------------\n")
            text_file.write(f"Winner: {winner}\n")
            text_file.write("-------------------------\n")
