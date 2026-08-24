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
4. Finds the location.
5. Gets the latitude and longitude.
6. Gets the weather using the coordinates.
7. Displays the weather.
8. Saves the result to a CSV file.

## Files

- `main.py` - starts the program
- `weather_search.py` - main program flow
- `weather_api.py` - API requests
- `user_input.py` - gets input from the user
- `validation.py` - checks the input
- `weather_csv.py` - saves the weather to CSV

## API Key

Create a `.env` file:

API_KEY=your_api_key

The `.env` file should not be uploaded to GitHub.

## Install

Install the packages:

```bash
pip install requests python-dotenv