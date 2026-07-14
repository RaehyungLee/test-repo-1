from functools import reduce


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


numbers = [1, 2, 3, 4, 5]

total = 0
for i in numbers:
    total += i

product = reduce(multiply, numbers, 1)


def main():
    print("sum:", total)
    print("product:", product)


if __name__ == "__main__":
    main()
