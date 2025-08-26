import requests

def main():
    url = "https://catfact.ninja/facts?page=1"
    response = requests.get(url)
    data = response.json()

    total = data["total"]
    per_page = data["per_page"]
    last_page = (total + per_page - 1) // per_page

    print(f"Всего фактов: {total}")
    print(f"Фактов на странице: {per_page}")
    print(f"Последняя страница: {last_page}")

    last_url = f"https://catfact.ninja/facts?page={last_page}"
    last_response = requests.get(last_url)
    last_data = last_response.json()

    facts = last_data["data"]
    
    shortest_fact = min(facts, key=lambda x: len(x["fact"]))["fact"]

    print("\nСамый короткий факт на последней странице:")
    print(shortest_fact)

if __name__ == "__main__":
    main()


