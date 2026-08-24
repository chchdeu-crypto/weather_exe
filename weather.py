import requests
import csv
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
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
    API_KEY=os.getenv("API_KEY")
    if state:
        location=f"{city},{state},{country}"
    else:
        location=f"{city},{country}"
    params={"q": location,"limit": 1,"appid": API_KEY}
    url="http://api.openweathermap.org/geo/1.0/direct"
    response=requests.get(url, params=params)
    data=response.json()
    lat=data[0]["lat"]
    lon=data[0]["lon"]
    if not data:
        return None
    return lat,lon
def get_weather(latitude, longitude):
    lat=latitude
    lon=longitude
    API_KEY=os.getenv("API_KEY")
    params={"lat": lat,"lon": lon,"appid": API_KEY}
    url="https://api.openweathermap.org/data/2.5/weather"
    response=requests.get(url, params=params)
    data=response.json()
    return data

def main():
    city=get_city()
    contry=get_country_code()
    get_weather(*get_location(city,contry))

main()


