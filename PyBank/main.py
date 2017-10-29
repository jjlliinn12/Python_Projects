# ## Option 1: PyBank

# ![Revenue](Images/revenue-per-lead.jpg)
#Import Dependencies
import os
import csv
#Read Csv File
# Read the csv file
csvpath = os.path.join(".","raw_data","budget_data_1.csv")
#test filepath
#print(csvpath)

# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will be given two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`). Each dataset is composed of two columns: `Date` and `Revenue`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# * The total number of months included in the dataset
total_months = 0
total_rev = []
second_list = []
change_in_revenue = []
# current_rev = 0
# next_rev = 0
# new_rev = 0
total_revenue = 0
print("Financial Analysis")
print("----------------------------")
with open(csvpath, newline="") as csvfile:
    #skip the headers
    reader = csv.reader(csvfile)
    next(reader, None)
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        total_months = total_months + 1
        total_rev.append(row[1])
        #total_revenue = total_revenue + (int(row['Revenues']))
    #print(total_revenue)
print("Total Months: " + str(total_months))
revenue = sum(map(int,total_rev))
print("Total Revenue: ${}".format(str(revenue)))
print (total_rev)
# for row in csvreader:
#     current_rev = csvreader[row[1]]
#     next_rev = csvreader[row+1]
#     new_rev = next_rev - current_rev
# print(str(new_rev))
for row in csvreader:
    second_list = second_list.append(row[2])
    change_in_revenue = list(zip(total_rev, second_list))
    zipped_list = change_in_revenue[:]    
#print(revenue_change)
# * The total amount of revenue gained over the entire period

# * The average change in revenue between months over the entire period
#print("Average Revenue Change: ${}".format(round((avg_rev))))
# * The greatest increase in revenue (date and amount) over the entire period

#print("Greatest Increase in Revenue: ${}".format())
#print("Greatest Increase in Revenue: ${}".format(str(greatest_increase)))
# * The greatest decrease in revenue (date and amount) over the entire period

#print("Greatest Decrease in Revenue: ${}".format())
# As an example, your analysis should look similar to the one below:

# ```
# Financial Analysis
# ----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)
# ```

# Your final script must be able to handle any such similarly structured dataset in the future (your boss is going to give you more of these -- so your script has to work for the ones to come). In addition, your final script should both print the analysis to the terminal and export a text file with the results.
