def process_list(lst):
    match lst:
        case []:
            return "Empty list"
        case [x]:
            return f"Single element: {x}"
        case [x, y]:
            return f"Two elements: {x}, {y}"
        case [x, *rest]:
            return f"First: {x}, Rest: {rest}"
        case [_, *middle, _]:
            return f"Middle section: {middle}"
        case _:
            return "Unhandled structure"

if __name__ == "__main__":
    print(process_list([]))  # Empty list
    print(process_list([42]))  # Single element: 42
    print(process_list([1, 2]))  # Two elements: 1, 2
    print(process_list([1, 2, 3, 4]))  # First: 1, Rest: [2, 3, 4]
    print(process_list("hello"))  # Unhandled structure
