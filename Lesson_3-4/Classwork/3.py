def power(mul):
    def square(func):
        def inner(a, b):
            var = func(a, b)
            return var ** mul
        return inner
    return square


@power(2)
def sum(a, b):
    return a + b


@power(3)
def dif(a, b):
    return a - b


c = sum(10, 20)
z = dif(15, 23)

print(c)
print(z)