"""PyBank Homework Starter File."""


"""Citations[some are copies, some are paraphrases]:

# calculating an average from standard library functions
[1]: https://www.geeksforgeeks.org/find-average-list-python/

# looping with an index using a for loop in python 
[2]: https://www.geeksforgeeks.org/python-range-function/

# Unzipping a tuple
[3]: https://book.pythontips.com/en/latest/zip.html

# list conversion from types in 1 list to types in another list
[4]: https://www.geeksforgeeks.org/python-convert-float-string-list-to-float-values/

"""

# Dependencies
import csv
import os

# functions

#function for an average; citation[1]
def average(list): 
    return sum(list)/ len(list)



# citation[2] for range function
def sequential_search_index(entry, list):
    for index in range(len(list)):
        if (list[index] == entry):
            return index
    return -1

def get_change_list(list):
    # define change_list
    change_list = []
    #stores first_value
    previous_value = list[0]
    # stores subsequent values as list
    subsequent_list = list[1:]
    for value in subsequent_list:
        # appends to change list. 
        change_list.append(value - previous_value)
        # reassigns for next loop
        previous_value = value
    return change_list


'''Files to load and output (update with correct file paths)'''
# please navigate to current working directory so that file input works.
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "budget_analysis.txt") # Output file path


"""Define variables to track the financial data"""
# running counters
total_months = 0
total_net = 0
# unzipped data
month_data = []
profit_data = []

# average profit change
average_change = 0

# greatest increase (month, profit) data
greatest_increase= ()
# greatest decrease (month, profit) data
greatestdecrease= ()

# indexes
month_index = 0
profit_index = 1

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=',')
    # Skip the header row
    header = next(reader)

    ''' Set up tracking P&L changes'''
    # unzipping reader tuple; see citation[3]
    month_data, profit_data_string = list(zip(*reader))

    # total months
    total_months += len(month_data)

    #profit_data list type conversion from string to float see citation[4] above
    profit_data = [float(entry) for entry in profit_data_string]
    # summing running total from changes list profit data; citation[1]
    profit_data_sum = sum(profit_data)
    # suming first month's baseline with running total profit_data_sum
    total_net += profit_data_sum

    # calculating average change from changes list profit data; citation[1]
        # get changes_list
    changes_list = get_change_list(profit_data)
    average_change = average(changes_list)

    # greatest increase in profit information
        # greatest increase in profit
    greatest_increase_value = max(changes_list)
        #index of greatest increase in profit
    greatest_increase_index = sequential_search_index(greatest_increase_value, changes_list)
        # month of greatest increase in profit
    greatest_increase_month = month_data[greatest_increase_index +1]
        #packing greatest increases in profit months and values
    greatest_increase = (greatest_increase_month, greatest_increase_value)

    # greatest decrease in profit information
        # greatest increase in profit
    greatest_decrease_value = min(changes_list)
        #index of greatest increase in profit
    greatest_decrease_index = sequential_search_index(greatest_decrease_value, changes_list)
        # month of greatest increase in profit
    greatest_decrease_month = month_data[greatest_decrease_index +1]
        #packing greatest increases in profit months and values
    greatest_decrease = (greatest_decrease_month, greatest_decrease_value)






# Print the output
    # assigning lines of text

textLines = ["Financial Analysis",
             "----------------------------",
             f"Total Months: {total_months:.0f}",
             f"Total: ${total_net:.0f}",
             f"Average Change: ${average_change:.2f}",
             f"Greatest Increase in Profits: {greatest_increase[month_index]} (${greatest_increase[profit_index]:.0f})",
             f"Greatest Decrease in Profits: {greatest_decrease[month_index]} (${greatest_decrease[profit_index]:.0f})"
            ]

    # printing output
for line in textLines:
    print(line)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    for line in textLines:
        txt_file.write(line + "\n")
