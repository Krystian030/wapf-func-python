import csv
from toolz import curry, pipe
from itertools import islice


def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            for row in csv.reader(csvfile):
                yield row
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error reading file: {e}")


# Curried functions for data processing
@curry
def extract_column(column_index, data):
    try:
        for row in data:
            yield row[column_index]
    except (IndexError, TypeError) as e:
        raise IndexError(f"Error extracting column: {e}")


@curry
def convert_to(converter, data):
    try:
        for item in data:
            yield converter(item)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Error converting values: {e}")


@curry
def skip_rows(num_rows, data):
    return islice(data, num_rows, None)


def calculate_average(column_values):
    total = 0
    count = 0

    for value in column_values:
        total += value
        count += 1

    if count == 0:
        raise ValueError("Error: Column values are empty.")

    return total / count


def main():
    csv_file_path = 'exampale.csv'
    score_column_index = 1
    header_row_index = 1

    score_column = extract_column(score_column_index)
    skip_header = skip_rows(header_row_index)
    convert_score_to_float = convert_to(float)

    try:
        print("Applying pipeline of operations (Lazy Evaluation)")
        average_result = pipe(
            read_csv_file(csv_file_path),  # Lazy file reading
            skip_header,  # Skip header rows (using curried skip_rows)
            score_column,  # Extract specific column
            convert_score_to_float,  # Convert values to float
            calculate_average  # Calculate the average
        )

        print(f"The average score is: {average_result}")
    except (FileNotFoundError, ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Pipeline error: {e}")


if __name__ == "__main__":
    main()
