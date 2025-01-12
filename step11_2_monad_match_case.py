import csv
import os

from returns.curry import curry
from returns.result import Success, Failure, Result


def read_csv_file(file_path: str) -> Result[list[list[str]], str]:
    if os.path.exists(file_path):
        with open(file_path, 'r') as csvfile:
            return Success([row for row in csv.reader(csvfile)])

    return Failure(f"Error reading file: {file_path}")


@curry
def extract_column(column_index: int, data: list[list[str]]) -> Result[list[str], str]:
    match data:
        case []:
            return Failure("Error: Data is empty")
        case _ if len(data[0]) > column_index:
            return Success([row[column_index] for row in data])


@curry
def remove_row(row_index: int, data: list[list[str]]) -> Result[list[list[str]], str]:
    match data:
        case []:
            return Failure("Error: Data is empty")
        case _ if len(data) > row_index:
            return Success(data[row_index:])


@curry
def convert_to(converter: callable, data: list[str]) -> Result[list[float], str]:
    match data:
        case []:
            return Failure("Error: Data is empty")
        case _:
            converted_data = [converter(item) if item.isdigit() else None for item in data]
            if all(x is not None for x in converted_data):
                return Success(converted_data)
            return Failure(f"Error: Unable to convert values to the specified type ({converter})")


def calculate_average(column_values: list[float]) -> Result[float, str]:
    match column_values:
        case []:
            return Failure("Error: Column values are empty")
        case _:
            return Success(sum(column_values) / len(column_values))


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

    match result:
        case Success(value):
            print(f"The average score is: {value}")
        case Failure(error):
            print(f"Pipeline error: {error}")


if __name__ == "__main__":
    main()
