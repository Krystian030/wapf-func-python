def apply_operation(operation, *args):
    return operation(*args)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def power(base, exponent):
    return base ** exponent

print(apply_operation(add, 3, 4))       # 7
print(apply_operation(multiply, 3, 4))  # 12
print(apply_operation(power, 2, 3))     # 8
