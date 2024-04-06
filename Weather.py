""" INSTALL THE Required Library

      pip install requests
     
"""



import requests


def get_weather(location):
    api_key = '8518b9346b4976483e2ddf23ff982695'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data


def display_weather(data):
    if data['cod'] == '404':
        print('City not found. Please check the spelling and try again.')
    else:
        city = data['name']
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        print(f'Weather in {city}: {weather_desc}')
        print(f'Temperature: {temp}°C')
        print(f'Humidity: {humidity}%')
def main():
    while True:
        location = input('Enter city name or Write quit to stop: ')
        if location.lower() =='quit':
            break
        weather_data = get_weather(location)
        display_weather(weather_data)

if __name__ == "__main__":
    main()
