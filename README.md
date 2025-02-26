Employee Data Processing

Overview
This project consists of multiple Python scripts designed to handle employee data. The scripts perform various tasks, including creating a dataset, identifying and cleaning missing values, and saving the cleaned data for further analysis.

Instructions

1. Creating Employee Data CSV

Script: create_employee_data_csv

Generates a CSV file named employee_data.csv.

Contains columns: EmployeeID, Name, Department, and Salary.

Includes eight rows of data, some with missing or incorrect values.

2. Loading Data and Identifying Missing Values

Script: load_and_identify_missing_values

Uses pandas to load employee_data.csv.

Identifies rows with missing values.

Displays the rows with missing data.

3. Filling Missing Salary Values

Script: load_and_fill_missing_salary

Loads the employee data.

Fills missing values in the Salary column using the mean salary of the existing records.

Outputs the updated DataFrame.

4. Cleaning Employee Data

Script: load_and_clean_employee_data

Removes duplicate rows based on the EmployeeID column.

Displays the cleaned DataFrame.

5. Saving the Cleaned Employee Data

Script: load_and_clean_employee_data_and_save

Saves the cleaned dataset to a new CSV file named cleaned_employee_data.csv.

Verifies and confirms the changes.

Prerequisites

Python 3.x

Pandas library (pip install pandas)

How to Run

Ensure Python and Pandas are installed.

Execute each script in the specified order to process and clean the employee data.

Verify the output in cleaned_employee_data.csv.

Author

[Bongane Ntombela]

