def compose(*functions):
    def composed_function(x):
        result = x
        for func in reversed(functions):
            result = func(result)
        return result
    return composed_function

def square(x):
    return x ** 2

def add_one(x):
    return x + 1

def double(x):
    return x * 2

def to_s(s):
    return f"final result {str(s)}"

pipeline = compose(to_s, square, add_one, double)
print(pipeline(3))  # final result 49
