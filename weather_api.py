import os
import requests
from dotenv import load_dotenv
load_dotenv()
def get_location(city, country, state=""):
    API_KEY=os.getenv("API_KEY")
    if state:
        location=f"{city},{state},{country}"
    else:
        location=f"{city},{country}"
    params={"q": location,"limit": 1,"appid": API_KEY}
    url="http://api.openweathermap.org/geo/1.0/direct"
    response=requests.get(url, params=params)
    try:
        response.raise_for_status()
    except requests.HTTPError:
        if response.status_code == 401:
            print("Invalid API key.")
        else:
            print(f"HTTP error: {response.status_code}")
        return None
    data=response.json()
    if not data:
        return None
    return data[0]
def get_weather(latitude, longitude):
    lat=latitude
    lon=longitude
    API_KEY=os.getenv("API_KEY")
    params={"lat": lat,"lon": lon,"appid": API_KEY,"units": "metric"}
    url="https://api.openweathermap.org/data/2.5/weather"
    try:
        response=requests.get(url, params=params)
        response.raise_for_status()
    except requests.HTTPError:
        if response.status_code == 401:
            print("Invalid API key")
        else:
            print(f"HTTP error: {response.status_code}")
        return None
    except requests.ConnectionError:
        print("Connection error")
        return None
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None
    data=response.json()
    return data