import requests

#Funtion to get weather information from Openweathermap API
def get_weather(city, api_key):
    base_url="https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data =response.json()

    if response.status_code == 200:
        return weather_data
    else:
        return None
    
#Main Program
if __name__ == "__main__":
    api_key ="acc22a71a13ad199323e6aa2055c4a09"

    while True:
        city = input("Enter a city name(or 'q' to quit):")
        if city.lower() == 'q':
            break
        weather_data = get_weather(city, api_key)


        if weather_data:
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            description = weather_data['weather'][0]['description']


            print(f"Weather in {city}: {description}")
            print(f"Tempreature: {temperature}C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("City not found , Please try again.")
