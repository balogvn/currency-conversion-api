import requests
import datetime

from bs4 import BeautifulSoup as bs
import re
from dateutil.parser import parse
from fastapi import FastAPI



api = FastAPI()
my_api_key = 'MY_API_KEY'
conversions = []




@api.get("/convert")

def convert(amount: float, from_currency: str, to_currency: str, apiKey: str):
    if apiKey != my_api_key:
        return{'msg': 'Invalid API key'}
    
    def get_digits(text):
        """Returns the digits and dots only from an input `text` as a float
        Args:
            text (str): Target text to parse
        """
        new_text = ""
        for c in text:
            if c.isdigit() or c == ".":
                new_text += c
        return float(new_text)

    url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={from_currency}&To={to_currency}"
    content = requests.get(url).content
    soup = bs(content, "html.parser")
    exchange_rate_html = soup.find_all("p")[2]
    exchange_rate = get_digits(exchange_rate_html.text)
    conversion = {
    "converted_amount": amount,
    'rate': exchange_rate,
    'metadata': {
        'time_of_conversion': str(datetime.datetime.now().isoformat()),
        'from_currency': from_currency,
        'to_currency': to_currency
    }}
    
    conversions.append(conversion)   
    return conversion



@api.get("/currencies")

def get_currencies(apiKey: str):
    if apiKey != my_api_key:
        return{'msg': 'Invalid API key'}
    cl_api_key = "a9517ee9935d3d60e71316f43dc85f6a"
    url = f"http://api.currencylayer.com/list?access_key={cl_api_key}&currencies=all"
    response = requests.get(url)
    return response.json()



@api.get("/history")
async def history(apiKey: str):
    if apiKey != my_api_key:
        return{'msg': 'Invalid API key'}
    
    return conversions



   
