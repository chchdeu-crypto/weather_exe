# Weather Project

This project gets weather information for a city.

The user enters:
- City
- Country code
- State code if the country is US

The program finds the location using the OpenWeather API and then gets the current weather.

## What the program does

1. Gets the city from the user.
2. Gets the country code.
3. Checks the input.
4. Gets a state code if the country is US.
5. Finds the location using the Geocoding API.
6. Gets the latitude and longitude.
7. Gets the current weather.
8. Processes the weather data.
9. Displays the weather.
10. Saves the result to a CSV file.

## Files

- main.py - starts the program
- weather_search.py - main program flow and weather processing
- weather_api.py - API requests
- user_input.py - gets input from the user
- validation.py - checks the input
- weather_csv.py - saves the weather results to CSV

## API Key

Create a .env file in the project folder.

API_KEY=your_api_key

The .env file should not be uploaded to GitHub.

## Install

Install the required packages:

pip install requests python-dotenv

## Run

python main.py

## Example

Enter city: Jerusalem
Enter country code: IL

City:Jerusalem
Country:IL
Temperature:27.4°C
Feels like:28.1°C
Condition:clear sky
Humidity:54%
Wind speed:3.6

For a US city:

Enter city: Austin
Enter country code: US
Enter state code: TX

## CSV

Successful weather searches are saved in weather_history.csv.

The file contains:

search_time, city, state, country, temperature, feels_like, condition, humidity, wind_speed

New results are added to the existing file without deleting previous results.

## Error handling

The program handles invalid input, location not found, invalid API keys, HTTP errors, request timeout, no internet connection, connection errors, other request errors, missing data in the API response, unexpected API response data, and CSV errors.

If an API request fails, the weather result is not saved to the CSV.

If the API response does not contain the expected data, the result is not saved.

If saving to the CSV fails, the weather information is still displayed.

## API

The project uses two API requests.

The first request uses the OpenWeather Geocoding API to find the location and get the coordinates.

The second request uses the OpenWeather Current Weather API to get the weather using the latitude and longitude.

The basic flow is:

User Input → Validation → Geocoding API → Latitude + Longitude → Weather API → Process Weather Data → Display Weather → Save to CSV