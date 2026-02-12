import requests
from sys import argv
from tavex_prices import get_tavex_prices
from tracker import get_gold_and_silver_prices


def send_message(token, chat_id, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    params = {
        'chat_id': chat_id,
        'text': message
    }
    resonse = requests.post(url, json=params)


def notify(token, chat_id):
    global_prices = get_gold_and_silver_prices()
    tavex_prices = get_tavex_prices()

    message = f'''
    Световни цени:
     - Злато: {global_prices.get('gold')} $
     - Сребро: {global_prices.get('silver')} $
    
Tavex цени:
     - Злато:
        продава: {tavex_prices.get('gold')[0]} €
        купува: {tavex_prices.get('gold')[1]} €
     - Сребро:
        продава: {tavex_prices.get('silver')[0]} €
        купува: {tavex_prices.get('silver')[1]} €
    '''

    send_message(token, chat_id, message)


if __name__ == '__main__':
    my_token = argv[1]
    my_chat_id = argv[2]

    notify(my_token, my_chat_id)
