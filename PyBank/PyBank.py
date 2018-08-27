import csv
# * The total number of months included in the dataset

# * The total amount of revenue gained over the entire period

# * The average change in revenue between months over the entire period

# * The greatest increase in revenue (date and amount) over the entire period

# * The greatest decrease in revenue (date and amount) over the entire period

# Files to load and output (Remember to change these)
file_to_load = "raw_data/budget_data_1.csv"
file_to_output = "analysis/budget_analysis_1.txt"

#Variables
total_months = 0

prev_revenue = 0

revenue_change_list = []

total_revenue = 0

greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:

        #Total Months
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])

        #Tracking revenue changes in order to have list to calculate average change over entire period
        revenue_change = int(row["Revenue"]) - prev_revenue
        prev_revenue = int(row["Revenue"])
        revenue_change_list = revenue_change_list + [revenue_change]

        #Calculate greatest increase in revenue over entire period
        if(revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change
        
        #Calculate greatest decrease
        if(revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change
        
#Calculate the average revenue change
revenue_average = sum(revenue_change_list) / len(revenue_change_list)

#Create Summary

summary = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_average}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

#Print Summary

print(summary)

# Export to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(summary)