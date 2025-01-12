import csv
from pyrsistent import pvector
from toolz import curry, pipe

# Function to handle file reading
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            return pvector([pvector(row) for row in csv.reader(csvfile)])
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error reading file: {e}")


# Curried functions for data processing
@curry
def extract_column(column_index, data):
    try:
        return pvector(row[column_index] for row in data)
    except (IndexError, TypeError) as e:
        raise IndexError(f"Error extracting column: {e}")


@curry
def remove_row(row_index, data):
    try:
        return data[row_index:]
    except (IndexError, TypeError) as e:
        raise IndexError(f"Error removing header: {e}")


@curry
def convert_to(converter, data):
    try:
        return pvector(converter(item) for item in data)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Error converting values: {e}")


# Function to calculate average (using Pattern Matching)
def calculate_average(column_values):
    match column_values:
        case [] | None:
            raise ValueError("Error: Column values are empty.")
        case _:
            try:
                return sum(column_values) / len(column_values)
            except ZeroDivisionError as e:
                raise ZeroDivisionError(f"Error calculating average: {e}")

def main():
    csv_file_path = 'example.csv'
    score_column_index = 1
    header_row_index = 1

    # Create pipeline steps
    score_column = extract_column(score_column_index)
    remove_header = remove_row(header_row_index)
    convert_score_to_float = convert_to(float)

    try:
        print("Applying pipeline of operations")
        average_result = pipe(
            read_csv_file(csv_file_path),
            score_column,
            remove_header,
            convert_score_to_float,
            calculate_average
        )
        print(f"The average score is: {average_result}")
    except (FileNotFoundError, ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Pipeline error: {e}")


if __name__ == "__main__":
    main()
