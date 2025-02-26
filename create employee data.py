import csv

def create_employee_data_csv():

    data = [
        ("employeeID", "Name", "Department", "Salary"),
        (1, "Nthabiseng Mofokeng", "Safety", 50000),
        (2, "Robert Ndwandwe", "IT", 60000),
        (3, "Mpumi Molefe", "Finance", ""),
        (4, "Tshenolo Ndlovu", "", 45000),
        (5, "Bongane Ntombela", "Sales", 84000),
        (6, "Alice White", "HR", 52000),
        (7, "Pholoso Ndlovu", "Safety", 57000),
        (8, "Thabang Mokwena", "Finance", ""),
        (9, "Thato Morena", "Sales", 40000),
        (10, "Rachel Ndlovu", "IT", 76000),
        (11, "Nthabiseng Mofokeng", "Safety", 50000),
        (7, "Pholoso Ndlovu", "Safety", 57000),
        (8, "Thabang Mokwena", "Finance", ""),
    ]

    try:
        with open("employee_data.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            # Crucial:  Handling potential empty strings more robustly
            for row in data:
                writer.writerow([str(cell) for cell in row])  # Converting to strings
        print("employee_data.csv file created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")

create_employee_data_csv()