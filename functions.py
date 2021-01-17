def who_am_i():
    name = "Me"
    age = 29
    print("Name " + name + " is old this much " + str(age))


who_am_i()


# With parameters
def add_one_hundred(num):
    print(num + 100)


add_one_hundred(1)


# Multiple Parameters
def add(x, y):
    print(x + y)


add(7, 7)


# Returning values
def multiply(x, y):
    return x * y


print(multiply(3, 7))


def square_root(x):
    return x ** .5


print(square_root(64))
