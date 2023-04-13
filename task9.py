def search_distribution(search_queries):
    distribution = {}
    for query in search_queries:
        words = query.split()
        if len(words) in distribution:
            distribution[len(words)] += 1
        else:
            distribution[len(words)] = 1
    total = len(search_queries)
    key_num = list(distribution)
    key_num.sort()
    for keys in key_num:
        percentage = round(distribution[keys] / total * 100, 2)
        if keys != 1:
            print(f"{keys} words: {percentage}%")
        else:
            print(f"{keys} word:  {percentage}%")


search_queries = ["watch new movies", "coffee near me", "how to find the determinant", "python",
                  "data science jobs in UK", "courses for data science", "taxi", "google", "yandex", "bing",
                  "foreign exchange rates USD/BYN", "Netflix movies watch online free",
                  "Statistics courses online from top universities"]
search_distribution(search_queries)
