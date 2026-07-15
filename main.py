from functools import reduce


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


numbers = [1, 1, 2, 3, 5, 8, 13]

total = reduce(add, numbers, 0)
product = reduce(multiply, numbers, 1)


def main():
    print("sum:", total)
    print("product:", product)


if __name__ == "__main__":
    main()
