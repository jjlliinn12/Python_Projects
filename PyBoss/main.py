import csv
import datetime
#Load File
file_to_load = "raw_data/employee_data2.csv"
#File to Output
file_to_output = "analysis/employee_data_reformatted2.csv"
#Dictionary for US State Abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Variables for re-formatted contents
emp_ids = []
emp_first_names = []
emp_last_names = []
emp_dobs = []
emp_ssns = []
emp_states = []

#Read Csv and convert to dictionary
with open(file_to_load) as emp_data:
    reader = csv.DictReader(emp_data)

    #Run Loop through each row
    for row in reader:
        
        #grab emp_ids and make list
        emp_ids = emp_ids + [row["Emp ID"]]
        
        #Grab and split employee names
        name_split = row["Name"].split(" ")

        #Save first and last name to two different lists
        emp_first_names = emp_first_names + [name_split[0]]
        emp_last_names  = emp_last_names + [name_split[1]]

        #Obtain Date of Birth
        new_dob = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
        new_dob = new_dob.strftime("%m/%d/%Y")

        #Store into list
        emp_dobs = emp_dobs + [new_dob]

        #Obtain SSN and hide first five digits
        split_ssn = list(row["SSN"])
        split_ssn[0:3] = ("*", "*", "*")
        split_ssn[4:6] = ("*", "*")
        join_ssn = "".join(split_ssn)

        #Store into list
        emp_ssns = emp_ssns + [join_ssn]

        #Retreive states and replace with state dictionary abbreviations
        state_ab = us_state_abbrev[row["State"]]

        #Store abbrevs into list
        emp_states = emp_states + [state_ab]

#Zip lists together
emp_records = zip(emp_ids, emp_first_names, emp_last_names, emp_dobs, emp_ssns, emp_states)

#Write into a new csv
with open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(emp_records)
