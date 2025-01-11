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
        return [row[column_index] for row in data]
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
        return [converter(item) for item in data]
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

    print(f"Extracting column index: {score_column_index}")
    score_column_values = extract_column(score_column_index, data)
    if score_column_values is None:
        print("Error: Could not extract column.")
        return

    print(f"Removing header row: {header_row_index}")
    removed_header_data = remove_row(header_row_index, score_column_values)
    if removed_header_data is None:
        print("Error: Could not remove header row.")
        return

    print("Converting column values to float")
    score_column_as_float = convert_to(float, removed_header_data)
    if score_column_as_float is None:
        print("Error: Could not convert column values to float.")
        return

    print("Calculating average for the column values")
    result = calculate_average(score_column_as_float)
    if result is None:
        print("Error: Could not calculate average.")
    else:
        print(f"The average is: {result}")


if __name__ == "__main__":
    main()
