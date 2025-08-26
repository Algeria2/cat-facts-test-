import requests

def main():
    # 1. Первый запрос - получаем первую страницу
    url = "https://catfact.ninja/facts?page=1"
    response = requests.get(url)
    data = response.json()

    total = data["total"]
    per_page = data["per_page"]
    last_page = (total + per_page - 1) // per_page

    print(f"Всего фактов: {total}")
    print(f"Фактов на странице: {per_page}")
    print(f"Последняя страница: {last_page}")

    # 2. Запрос последней страницы
    last_url = f"https://catfact.ninja/facts?page={last_page}"
    last_response = requests.get(last_url)
    last_data = last_response.json()

    facts = last_data["data"]

    # 3. Поиск самого короткого факта
    shortest_fact = min(facts, key=lambda x: len(x["fact"]))["fact"]

    print("\nСамый короткий факт на последней странице:")
    print(shortest_fact)

if __name__ == "__main__":
    main()