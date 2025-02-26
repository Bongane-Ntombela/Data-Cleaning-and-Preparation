import pandas as pd

def load_and_clean_employee_data_and_save():

    try:
        file_path = pd.read_csv("employee_data.csv")

        print("Original DataFrame:")
        print(file_path)

        try:
            mean_salary = file_path['Salary'].astype(float).mean()
            file_path['Salary'] = file_path['Salary'].astype(float).fillna(mean_salary)
        except (TypeError, ValueError) as e:
            print(f"Error calculating or filling salary: {e}")
            print("Cannot proceed with cleaning due to non-numeric data in the 'Salary' column.")
            return

        file_path = file_path.drop_duplicates(subset=['employeeID'], keep='first')

        # Displaying cleaned DataFrame
        print("\nCleaned DataFrame (duplicates removed):")
        print(file_path)

        file_path.to_csv("cleaned_employee_data.csv", index=False)
        print("\nCleaned data saved to cleaned_employee_data.csv")


    except FileNotFoundError:
        print(f"Error: File 'employee_data.csv' not found.")
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



load_and_clean_employee_data_and_save()