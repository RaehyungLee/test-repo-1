"""Shared aggregation helper (partner PR variant)."""


def combine(values):
    total = 0
    for value in values:
        total += value
    return total
