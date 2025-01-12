import csv

from pyrsistent import pvector
from toolz import curry, pipe


# Function to handle file reading
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            return pvector([pvector(row) for row in csv.reader(csvfile)])
    except FileNotFoundError:
        print("Error: File not found.")
        return None


# Curried functions for data processing
@curry
def extract_column(column_index, data):
    try:
        return pvector(row[column_index] for row in data)
    except IndexError:
        print("Error: Column index out of range.")
        return None


@curry
def remove_row(row_index, data):
    try:
        return data[row_index:]
    except IndexError:
        print("Error: Row index out of range.")
        return None


@curry
def convert_to(converter, data):
    try:
        return pvector(converter(item) for item in data)
    except ValueError:
        print("Error: Failed to convert values.")
        return None


# Function to calculate average
def calculate_average(column_values):
    if not column_values:
        print("Error: Column values are empty.")
        return None
    try:
        average = sum(column_values) / len(column_values)
        return average
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None


def main():
    csv_file_path = 'example.csv'
    score_column_index = 1
    header_row_index = 1

    print("Applying pipeline of operations")
    average_result = pipe(
        read_csv_file(csv_file_path),
        extract_column(score_column_index),
        remove_row(header_row_index),
        convert_to(float),
        calculate_average
    )

    if average_result is None:
        print("Error: Could not complete processing.")
    else:
        print(f"The average score is: {average_result}")


if __name__ == "__main__":
    main()
