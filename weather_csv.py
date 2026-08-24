import csv
import os
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