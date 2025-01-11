from pyrsistent import pvector

def demonstrate_immutability():
    immutable_list = pvector([1, 2, 3, 4])
    print("Original immutable_list:", immutable_list)

    try:
        immutable_list[0] = 99
    except TypeError as e:
        print("Error when trying to modify immutable_list:", e)

    new_immutable_list = immutable_list.append(5)
    print("Immutable list after appending:", new_immutable_list)
    print("Original immutable_list remains unchanged:", immutable_list)

if __name__ == "__main__":
    demonstrate_immutability()
