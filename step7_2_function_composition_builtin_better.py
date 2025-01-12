from functools import partial, reduce
from typing import Callable


def multiply_by_n(data: list[int], n: int) -> list[int]:
    return [item * n for item in data]


def add_n(data: list[int], n: int) -> list[int]:
    return [item + n for item in data]


type Composable[T] = Callable[[T], T]


def compose[T](*functions: Composable[T]) -> Composable[T]:
    def apply(value: T, fn: Composable[T]) -> T:
        return fn(value)

    return lambda data: reduce(apply, functions, data)


def main():
    data = [1, 5, 3, 4, 2]
    print(f"Data before: {data}") # Data before: [1, 5, 3, 4, 2]

    multiply_by_2 = partial(multiply_by_n, n=2)
    add_10 = partial(add_n, n=10)
    do_operations = compose(multiply_by_2, add_10)

    result = do_operations(data)
    print(f"Result: {result}") # Result: [12, 14, 16, 20, 22]


if __name__ == "__main__":
    main()
