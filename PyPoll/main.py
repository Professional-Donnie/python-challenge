# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

"""
Citations

# looping with an index using a for loop in python 
[0]:https://www.geeksforgeeks.org/python-range-function/

# more information on the in operator and using it for comparisons. 
[1]: https://www.geeksforgeeks.org/python-get-unique-values-list/#
[2]: https://realpython.com/python-in-operator/#:~:text=in%20data%20types.-,Using%20in%20and%20not%20in%20With%20Different%20Python%20Types,dictionaries%20also%20support%20these%20tests.


[3]: https://www.programiz.com/python-programming/methods/built-in/dict


"""

# Import necessary modules
import csv
import os

# functions

def vote_incrementor(candidates_list, name): 
    # loops through each index in candidates_list; citation[0]
    for index in range(len(candidates_list)):
        # compares value in name to value in dictionary with key 'name'; citation[1], citation[2]
        if name in candidates_list[index]['name']:
            # increments vote count in dictionary with key: 'vote_count'
            candidates_list[index]['vote_count'] +=1
    return candidates_list
    



# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
list_of_candidate_names = []
list_of_candidate_dictionaries = []

# gives an example of what the candidate dictionary will look like, citation[3]
candidate_example = dict(name="", vote_count = 0, vote_percentage = 0.0)


# Winning Candidate and Winning Count Tracker
winner = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes+=1

        # Get the candidate's name from the row
        candidate_name=row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in list_of_candidate_names:
            list_of_candidate_names.append(candidate_name)
            #citation[3]
            candidate = dict(name=candidate_name, vote_count = 0, vote_percentage = 0.0)
            list_of_candidate_dictionaries.append(candidate)    

        # Add a vote to the candidate's count
        list_of_candidate_dictionaries = vote_incrementor(list_of_candidate_dictionaries, candidate_name)


# finish list_of_candidate_dictionaries percentages
for candidate in list_of_candidate_dictionaries:
    candidate['vote_percentage'] = (candidate['vote_count']/ total_votes) * 100  


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # list of lines of text
    textLines = []
    # make a new line
    print("\n")

    # Print the total vote count (to terminal)
    print("Election Results")
    # append to lines of text
    textLines.append("Election Results")

    print("-------------------------")
    # append to lines of text
    textLines.append("-------------------------")

    # Write the total vote count to the text file
    print(f"Total Votes: {total_votes}")

    textLines.append(f"Total Votes: {total_votes}")

    print("-------------------------")
    textLines.append("-------------------------")


    # Loop through the candidates to determine vote percentages and identify the winner
        # Get the vote count and calculate the percentage
    winner_count = 0
    for candidate in list_of_candidate_dictionaries:
        candidate['vote_percentage'] = (candidate['vote_count']/ total_votes) * 100  
        # Print and save each candidate's vote count and percentage
        print(f"{candidate["name"]}: {candidate['vote_percentage']:.3f}% ({candidate['vote_count']})")
        # append to lines of text
        textLines.append(f"{candidate["name"]}: {candidate['vote_percentage']:.3f}% ({candidate['vote_count']})")
        # Update the winning candidate if this one has more votes
        if (candidate['vote_count'] > winner_count):
            winner = candidate['name']
            winner_count = candidate['vote_count']

    print("-------------------------")
    textLines.append("-------------------------")


    # Generate and print the winning candidate summary
    print(f"Winner: {winner}")
    textLines.append(f"Winner: {winner}")

    
    print("-------------------------")
    textLines.append("-------------------------")


    # Save the winning candidate summary to the text file
    for line in textLines: 
        txt_file.write(line + "\n")