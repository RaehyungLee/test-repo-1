from functools import reduce


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


numbers = [1, 8, 27, 64, 125]

total = reduce(add, numbers, 0)
product = reduce(multiply, numbers, 1)


def main():
    print("sum:", total)
    print("product:", product)


if __name__ == "__main__":
    main()
