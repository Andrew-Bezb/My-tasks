from math import comb


def kosti(n, m, s):
    p = (7 - s) / 6  # не менее s
    result = comb(n, m) * p ** m * (1 - p) ** (n - m)
    return result
