import requests
from talk import talk, talkG

api_key = '72f6a957c3df52e551d2f037cb3b6ae7'
base_url = 'https://api.openweathermap.org/data/2.5/weather?'


def getWeather(s1):
    try:
        s1 = s1.split(' ')
        city_name = s1[-1]
        city_name = city_name.capitalize()
        url = f'{base_url}appid={api_key}&q={city_name}'
        response = requests.get(url)
        x = response.json()
        weather = x['weather']
        print(weather)
        minTemp = x['main']['temp_min']
        # minTemp = (minTemp - 32) * (5 / 9)
        minTemp = minTemp - 273
        minTemp = "{:.2f}".format(minTemp)
        maxTemp = x['main']['temp_max']
        maxTemp = maxTemp - 273
        # maxTemp = (maxTemp - 32) * (5 / 9)
        maxTemp = "{:.2f}".format(maxTemp)
        feelsLike = x['main']['feels_like']
        feelsLike = feelsLike - 273
        # feelsLike = (feelsLike - 32) * (5 / 9)
        feelsLike = "{:.2f}".format(feelsLike)
        # pressure = x['main']['pressure']
        humidity = x['main']['humidity']
        talk(f'The minimum temperature at {city_name} today will be {minTemp} degrees')
        talk(f'The max temp will be {maxTemp} degrees')
        talk(f'It feels like {feelsLike} degrees now at {city_name}')
        # talk(f'The atmospheric pressure will be {pressure} ATM')
        talk(f'The humidity will be {humidity} percent today.')
    except:
        talk(f'I could not get any weather updates for {city_name}')
