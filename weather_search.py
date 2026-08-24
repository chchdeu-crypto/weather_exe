from datetime import datetime
from user_input import*
from validation import*
from weather_api import get_location, get_weather
from weather_csv import save_weather_to_csv
def process_weather_data(location,weather):
    search_time=datetime.now()
    city=location["name"]
    try:
        state=location["state"]
    except KeyError:
        state=""
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
