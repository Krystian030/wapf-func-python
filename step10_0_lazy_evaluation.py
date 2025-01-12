def multiply_by_x(data, x):
    for item in data:
        yield item * x


def main():
    data = iter([1, 5, 3, 4, 2])

    multiply_by_2 = multiply_by_x(data, 2)
    print(f"Type: {type(multiply_by_2)}")  # <class 'generator'>
    for _ in range(3):
        print(next(multiply_by_2))


if __name__ == "__main__":
    main()
