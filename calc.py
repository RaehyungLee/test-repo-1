from functools import reduce

numbers = [1, 2, 3, 4]


def aggregate(values):
    return {
        "total": reduce(lambda acc, n: acc + n, values, 0),
        "product": reduce(lambda acc, n: acc * n, values, 1),
        "max": max(values),
    }


stats = aggregate(numbers)

print("sum:", stats["total"])
print("product:", stats["product"])
print("max:", stats["max"])

# re-scan trigger
