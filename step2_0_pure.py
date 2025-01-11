
def pure_add(x, y):
    return x + y

some_global = 0
def not_so_pure_add(x):
    global some_global
    print(f"Adding {x} to {some_global}")
    some_global += x
    return some_global

def main():
    print(f"Pure add: {pure_add(1, 2)}")
    print(f"Not so pure add: {not_so_pure_add(1)}")
    print(f"Not so pure add: {not_so_pure_add(2)}")

if __name__ == "__main__":
    main()