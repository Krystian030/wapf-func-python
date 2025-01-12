from abc import ABC, abstractmethod


class Maybe(ABC):

    def is_some(self):
        return isinstance(self, Some)

    def is_nothing(self):
        return isinstance(self, Nothing)

    @abstractmethod
    def bind(self, func):
        pass


class Some(Maybe):
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        return func(self.value)

    def __str__(self):
        return f"Some({self.value})"


class Nothing(Maybe):
    def bind(self, _):
        return self

    def __str__(self):
        return "Nothing"


def divide(a, b):
    return Some(a / b) if b != 0 else Nothing()


def main():
    result = (
        Some(10)
        .bind(lambda x: divide(x, 2))
        .bind(lambda x: divide(x, 0))  # This will return Nothing
        .bind(lambda x: divide(x, 4))
    )
    print(f"Result: {result}")  # Nothing

    result = (
        Some(10)
        .bind(lambda x: divide(x, 2))
        .bind(lambda x: divide(x, 5))
    )
    print(f"Result: {result}")  # Some(1.0)

    # Expression: m >>= (\x -> f x >>= g)
    result_left = (
        Some(12)
        .bind(lambda x: divide(x, 2).bind(lambda y: divide(y, 3)))
    )

    # Expression: (m >>= f) >>= g
    result_right = (
        Some(12)
        .bind(lambda x: divide(x, 2))
        .bind(lambda y: divide(y, 3))
    )

    print(f"Left result: {result_left}, Right result: {result_right}")


if __name__ == "__main__":
    main()
