import requests
import csv
import os
from datetime import datetime
from dotenv import load_dotenv
import csv
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

def get_state_code():
    state_code=input("Enter state code: ").upper().strip()
    return state_code
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

def process_weather_data(location,weather):
    search_time=datetime.now()
    city=location["name"]
    state=location["state"]
    country=location["country"]
    temperature=weather["main"]["temp"]
    feels_like=weather["main"]["feels_like"]
    condition=weather["weather"][0]["description"]
    humidity=weather["main"]["humidity"]
    wind_speed=weather["wind"]["speed"]
    weather_result={"search_time":str(search_time),"city":city,"state":state,"country":country,"temperature":temperature,"feels_like":feels_like,"condition":condition,"humidity":humidity,"wind_speed":wind_speed}
    return weather_result

def print_weather(weather_result):
    print(f"City:{weather_result["city"]}")
    print(f"Country:{weather_result["country"]}")
    print(f"Temperature:{weather_result["temperature"]}\u00B0C")
    print(f"Feels like:{weather_result["feels_like"]}\u00B0C")
    print(f"Condition:{weather_result["condition"]}")
    print(f"Humidity:{weather_result["humidity"]}%")
    print(f"Wind speed:{weather_result["wind_speed"]}")
    if weather_result["state"]!="":
        print(f"State/Region:{weather_result["state"]}")

def save_weather_to_csv(weather_result):
    filename = "weather_history.csv"
    file_exists = os.path.exists(filename)
    try:
        with open(filename,"a",newline="") as file:
            fields=["search_time", "city", "state", "country","temperature", "feels_like", "condition","humidity", "wind_speed"]
            writer=csv.DictWriter(file,fieldnames=fields)
            if not file_exists:
                writer.writeheader()
            writer.writerow(weather_result)
        return True
    except Exception as e:
        print(type(e).__name__)
        return False

def run():
    city=get_city()
    if not check_not_empty_input(city):
        raise_on_empty()
    contry=get_country_code()
    if not check_not_empty_input(contry):
            raise_on_empty()
    if not check_len_input(contry):
        raise_on_len()
    if not check_if_us(contry):
        loction=get_location(city,contry)
    else:
        loction=get_location(city,contry,get_state_code())
    if not loction:
        print("Location not found")
        return
    lat=loction["lat"]
    lon=loction["lon"]
    weather=get_weather(lat,lon)
    weather_result=process_weather_data(loction,weather)
    print_weather(weather_result)
    saved=save_weather_to_csv(weather_result)
    if saved:
        print("Weather result saved to weather_history")
    else:
        print("The weather was received, but it could not be saved")
run()

