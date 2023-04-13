def f(x):
    return 3 * x ** 3 + 4 * x ** 2 + 5 * x + 21


def find_minimum(a, b, eps):  # Метод деления пополам
    while abs(b - a) > eps:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return round((a + b) / 2, len(str(eps)) - 2)


print(find_minimum(-10, 10, 0.01))