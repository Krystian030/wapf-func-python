import csv

# Function to handle file reading
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        return None

# Function to extract a column
def extract_column(column_index, data):
    try:
        column_values = [float(row[column_index]) for row in data[1:]]
        return column_values
    except (ValueError, IndexError):
        return None

# Function to calculate average
def calculate_average(column_values):
    if not column_values:
        return None
    try:
        average = sum(column_values) / len(column_values)
        return average
    except ZeroDivisionError:
        return None

def main():
    # Data pipeline
    csv_file_path = 'example.csv'
    column_index = 1

    # Step 1: Read CSV file
    print(f"Reading CSV file from path: {csv_file_path}")
    data = read_csv_file(csv_file_path)
    if data is None:
        print("Error: Could not read CSV file.")
        return

    # Step 2: Extract column
    print(f"Extracting column index: {column_index}")
    score_column_values = extract_column(column_index, data)
    if score_column_values is None:
        print("Error: Could not extract column.")
        return

    # Step 3: Calculate average
    print("Calculating average for the column values")
    result = calculate_average(score_column_values)
    if result is None:
        print("Error: Could not calculate average.")
    else:
        print(f"The average is: {result}")

if __name__ == "__main__":
    main()
