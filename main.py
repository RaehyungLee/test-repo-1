from functools import reduce


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


numbers = [31, 37, 41, 43, 47]

total = reduce(add, numbers, 0)
product = reduce(multiply, numbers, 1)


def main():
    print("sum:", total)
    print("product:", product)


if __name__ == "__main__":
    main()
