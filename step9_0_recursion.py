import sys
from random import randint
from time import perf_counter_ns

sys.setrecursionlimit(10 ** 9)


def sum_recursive(data: list[int], number_of_elements: int) -> int:
    match number_of_elements:
        case 0:
            return 0
        case _:
            return data[number_of_elements - 1] + sum_recursive(data, number_of_elements - 1)


def sum_iterative(data: list[int]) -> int:
    total = 0
    for number in data:
        total += number

    return total


def main():
    data = [randint(0, 1_000_000) for _ in range(1_000_000)]

    start = perf_counter_ns()
    result_recursive = sum_recursive(data, len(data))
    time_recursive_in_s = (perf_counter_ns() - start) / 1e9

    start = perf_counter_ns()
    result_iterative = sum_iterative(data)
    time_iterative_in_s = (perf_counter_ns() - start) / 1e9

    print(f"Recursive sum: {result_recursive} in {time_recursive_in_s} seconds")
    print(f"Iterative sum: {result_iterative} in {time_iterative_in_s} seconds")


if __name__ == "__main__":
    main()
