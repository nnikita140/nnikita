import requests
from bs4 import BeautifulSoup
import pickle

url = "https://quotes.toscrape.com/"

def extract_quotes(soup):
    quotes = []

    blocks = soup.find_all("div", class_="quote")
    print("Найдено блоков:", len(blocks))  # ← контроль

    for block in blocks:
        text = block.find("span", class_="text").get_text(strip=True)
        author = block.find("small", class_="author").get_text(strip=True)

        quotes.append({
            "text": text,
            "author": author
        })

    return quotes


def fetch_quotes():
    response = requests.get(url, timeout=10)
    print("Status:", response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")
    return extract_quotes(soup)


def save_quotes(quotes, filename="quotes.pickle"):
    with open(filename, "wb") as f:
        pickle.dump(quotes, f)
    print(f"Сохранено {len(quotes)} цитат")


quotes = fetch_quotes()
print("Итого:", len(quotes))
save_quotes(quotes)
