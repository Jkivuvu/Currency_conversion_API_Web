import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get('API_KEY')
url2 = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
response = requests.get(url2)
currencies = response.json()['conversion_rates']
currencies_list = [currency for currency in currencies]
currencies_list2 = [currency for currency in currencies]






