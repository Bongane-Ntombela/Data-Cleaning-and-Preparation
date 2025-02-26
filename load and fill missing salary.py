import pandas as pd

def load_and_fill_missing_salary():

    try:
        file_path = pd.read_csv("employee_data.csv")

        print("Original DataFrame:")
        print(file_path)

        try:
          mean_salary = file_path['Salary'].mean()
        except TypeError:
          print("Error: Cannot calculate mean; Salary column contains non-numeric values.")
          return 

        file_path['Salary'] = file_path['Salary'].fillna(mean_salary)

        print("\nDataFrame with filled missing salaries:")
        print(file_path)

    except FileNotFoundError:
        print(f"Error: File 'employee_data.csv' not found.")
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
    except Exception as e:
        print(f"Error loading or processing file: {e}")


load_and_fill_missing_salary()