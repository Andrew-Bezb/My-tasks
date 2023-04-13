import random


def central_tendency_distribution(distribution):
    mean = sum(distribution) / len(distribution)
    mode = max(set(distribution), key=distribution.count)
    sorted_dist = sorted(distribution)
    # print(sorted_dist)     #для просмотра списка
    if len(sorted_dist) % 2 == 0:
        median = (sorted_dist[len(sorted_dist) // 2] + sorted_dist[len(sorted_dist) // 2 - 1]) / 2
    else:
        median = sorted_dist[len(sorted_dist) // 2]
    print(f"Среднее: {mean}")
    print(f"Мода: {mode}")
    print(f"Медиана: {median}")
    if mean == median:
        print("Распределение симметрично")
    elif mean < median:
        print("Распределение асимметрично вправо")
    else:
        print("Распределение асимметрично влево")


distribution = [random.randint(1, 100) for i in range(150)]
central_tendency_distribution(distribution)