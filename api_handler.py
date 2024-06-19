# 3. API Request Handler:

# Build a program that makes requests to a public API and handles exceptions for network errors, 
# invalid responses, and rate limits.


import requests

def know_weather(city):
    api_key = "89628211d24da79c6fd48653c5f93696" # OpenWeatherMap API key from https://home.openweathermap.org/api_keys
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key}
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data.get('cod') == 429: # This is a way to access a key called 'cod' in the data object. 429 is the http status code for too many requests. rate limit exceeded
            print("Rate limit exceeded, please try again later")
            return None
        
        return data
    
    except requests.exceptions.RequestException:
        print(f"Request error found")
        return None


city = input("Enter a city: ")
weather_data = know_weather(city)

print(weather_data)
    
if weather_data:
    print(f"Weather in {city} at the moment: {weather_data['weather'][0]['description']}")
else:
    print("Failed to retrieve weather data")

 