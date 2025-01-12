def plus(a):
    def add(b):
        return a + b
    return add

result = plus(2)(3) # 5
# Partial apply, transform binary function to unary function
plusTwo = plus(2)
print(plusTwo(3)) # 5
