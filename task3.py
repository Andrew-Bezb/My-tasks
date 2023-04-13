from datetime import datetime

print('Вводите даты в формате дд.мм.гг')


def date_diff(date1, date2):
    diff = (datetime.strptime(date2, "%d.%m.%Y") - datetime.strptime(date1, "%d.%m.%Y")).days
    if diff < 0:
        diff = abs(diff)
        return f"Абсолютное значение разницы между датами: {diff} дней"
    return diff


print(date_diff("13.12.2003", "13.04.2023"))
