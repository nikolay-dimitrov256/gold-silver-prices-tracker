import requests
from bs4 import BeautifulSoup


def get_tavex_price(url: str) -> tuple[float|None, float|None]:
    response = requests.get(url)

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    sell_span_element = soup.find('span', class_='product-poster__pricelist-value')
    sell_price_data = sell_span_element.text.split()

    buy_span_elements = soup.find_all('span', class_='product-poster__table-label product-poster__table-label--2')

    for element in buy_span_elements:
        if '€' in element.text:
            buy_price_eur = float(element.text.replace('€', '').replace(',', '.').strip().split()[0])
            break
    else:
        buy_price_eur = None

    sell_price_eur = float(sell_price_data[0].replace(',', '.'))

    return sell_price_eur, buy_price_eur


def get_tavex_prices() -> dict:
    urls = {
        'gold': 'https://tavex.bg/zlato/1-unciya-zlatna-moneta-avstraliysko-kenguru/',
        'silver': 'https://tavex.bg/srebro/1-unciya-srebarna-moneta-dds-marja-razlichni-vidove/',
    }

    tavex_prices = {}

    for asset, url in urls.items():
        prices = get_tavex_price(url)
        tavex_prices[asset] = prices

    return tavex_prices