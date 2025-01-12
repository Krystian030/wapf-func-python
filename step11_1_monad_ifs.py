import csv
import os

from returns.curry import curry
from returns.pipeline import is_successful
from returns.result import Success, Failure


def read_csv_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as csvfile:
            return Success([row for row in csv.reader(csvfile)])

    return Failure(f"Error reading file: {file_path}")


@curry
def extract_column(column_index, data):
    if len(data) > column_index:
        return Success([row[column_index] for row in data])

    return Failure(f"Error extracting column: {column_index}")


@curry
def remove_row(row_index, data):
    if len(data) > row_index:
        return Success(data[row_index:])

    return Failure(f"Error: Unable to remove rows up to index {row_index}")


@curry
def convert_to(converter, data):
    converted_data = [converter(item) if item.isdigit() else None for item in data]
    if all(x is not None for x in converted_data):
        return Success(converted_data)

    return Failure(f"Error: Unable to convert values to the specified type ({converter})")


def calculate_average(column_values):
    if len(column_values) > 0:
        return Success(sum(column_values) / len(column_values))

    return Failure("Error: Division by zero")


def main():
    csv_file_path = 'example.csv'
    score_column_index = 1
    header_row_index = 1

    result = (
        read_csv_file(csv_file_path)
        .bind(remove_row(header_row_index))
        .bind(extract_column(score_column_index))
        .bind(convert_to(float))
        .bind(calculate_average)
    )

    if is_successful(result):
        print(f"The average score is: {result.unwrap()}")
    else:
        print(f"Pipeline error: {result.failure()}")


if __name__ == "__main__":
    main()
