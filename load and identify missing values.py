import pandas as pd

def load_and_identify_missing_values():
    
    try:
        file_path = pd.read_csv("employee_data.csv")
        
        print("Original DataFrame:")
        print(file_path)
        
        missing_values = file_path[file_path.isnull().any(axis=1)]
        
        if missing_values.empty:
            print("\nNo missing values found.")
        else:
            print("\nRows with missing values:")
            print(missing_values)
    
    except FileNotFoundError:
        print(f"Error: File 'employee_data.csv' not found.")
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
    except Exception as e:
        print(f"Error loading or processing file: {e}")

load_and_identify_missing_values()