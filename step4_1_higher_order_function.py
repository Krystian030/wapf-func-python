import csv

from pyrsistent import pvector


# Function to handle file reading
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            return pvector([pvector(row) for row in reader])
    except FileNotFoundError:
        return None


# Higher-order function to apply a sequence of operations
def apply_pipeline(data, operations):
    for operation in operations:
        data = operation(data)
        if data is None:
            break  # Stop pipeline on failure

    return data


# Function to extract a column
def extract_column(column_index, data):
    try:
        return pvector(row[column_index] for row in data)
    except IndexError:
        return None


# Remove a specific number of rows (e.g., the header row)
def remove_row(row_index, data):
    try:
        return data[row_index:]
    except IndexError:
        return None


# Convert data to a specific type (e.g., float)
def convert_to(converter, data):
    try:
        return pvector(converter(item) for item in data)
    except ValueError:
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
    csv_file_path = 'example.csv'
    score_column_index = 1
    header_row_index = 1

    print(f"Reading CSV file from path: {csv_file_path}")
    data = read_csv_file(csv_file_path)
    if data is None:
        print("Error: Could not read CSV file.")
        return

    # Define pipeline of operations
    operations = [
        lambda data: extract_column(score_column_index, data),  # Extract column
        lambda data: remove_row(header_row_index, data),  # Remove header row
        lambda data: convert_to(float, data)  # Convert to float
    ]

    print("Applying pipeline of operations")
    processed_data = apply_pipeline(data, operations)
    if processed_data is None:
        print("Error: Could not process data.")
        return

    print("Calculating average for the column values")
    result = calculate_average(processed_data)
    if result is None:
        print("Error: Could not calculate average.")
    else:
        print(f"The average is: {result}")


if __name__ == "__main__":
    main()
