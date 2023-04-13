def calculate_success_prob(deal_success, current_profit):
    success_count = len([x for x in deal_success if x > 0])  # количество успешных сделок
    total_count = len(deal_success)  # общее количество сделок
    success_prob = (success_count / total_count) * 100

    total_profit = sum(deal_success) + current_profit  # чистый доход инвестора
    initial_capital = 1000  # первоначальный капитал
    roi = ((total_profit + initial_capital) / initial_capital) * 100  # ROI в %

    print(f"Вероятность успеха сделки: {round(success_prob, 2)}%")
    print(f"Чистый доход (убыток) инвестора: {total_profit}")
    print(f"ROI: {round(roi, 1)}%")
