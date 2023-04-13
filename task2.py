from math import sqrt


def cosin(a, b):
    if len(a) != len(b):
        raise ValueError('вектора разной длины!')
    if not sum(a) or not sum(b):
        raise ValueError('нулевой вектор!')
    return sum([a[i] * b[i] for i in range(len(a))]) / (
            sqrt(sum([a[i] ** 2 for i in range(len(a))])) * sqrt(sum([b[i] ** 2 for i in range(len(a))])))
