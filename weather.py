import requests
import csv
import os
from datetime import datetime
from dotenv import load_dotenv

def get_city():
    city=input("Enter city: ").strip()
    return city

def get_country_code():
    country_code=input("Enter country code: ").strip().upper()
    return country_code

def check_not_empty_input(txt):
    return txt !="" 

def check_len_input(txt):
    return len(txt)==2

def raise_on_empty():
    raise ValueError("input ust not be empty")

def raise_on_len():
    raise ValueError("input most contine 2 letters")

def check_if_us(txt):
    return txt == "US"

def state_code():
    state_code=input("Enter_state_code: ")

def get_location(city, country, state=""):
    load_dotenv()
    API_KEY=os.getenv("API_KEY")
    if state:
        location=f"{city},{state},{country}"
    else:
        location=f"{city},{country}"
    params={"q": location,"limit": 1,"appid": API_KEY}
    url="http://api.openweathermap.org/geo/1.0/direct"
    response=requests.get(url, params=params, timeout=10)
    data=response.json()
    if not data:
        return None
    return data
def main():
    city=get_city()
    contry=get_country_code()
    get_location(city,contry)
main()


