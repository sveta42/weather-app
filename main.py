import requests, json
import datetime
#sample values for testing
def findcitylines(city):
    API_key = 'c5008a5fabe7ef11292903e0d3cc043e'
    limit = 5
    #final url for testing
    geocoding_URL = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={API_key}'
    #opening the url and getting the info from it
    geo_response = requests.get(geocoding_URL)
    geo_data = geo_response.json()
    cor_lines = {'city_lat': geo_data[0]['lat'], 'city_lon': geo_data[0]['lon']}
    return templist(cor_lines)

def templist(cor_lines):
    lat = cor_lines['city_lat']
    lon = cor_lines['city_lon']
    API_key2 = '99ed56942269af6c4abedb3bc02d2795'
    part = 'current,minutely,hourly,alerts'
    units = 'metric'
    weather_URL = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_key2}&units={units}'
    wea_response = requests.get(weather_URL)
    wea_data = wea_response.json()

    today = datetime.datetime.now()
    dates_7 = [(today + datetime.timedelta(days=i)).strftime("%d/%m") for i in range(7)]

    temp_day = {}
    for day in range(0,7):
        temp_day[day] = {'date': dates_7[day],
                         'max_temp': wea_data['daily'][day]['temp']['max'],
                         'min_temp': wea_data['daily'][day]['temp']['min'],
                         'humidity': wea_data['daily'][day]['humidity']}
    return temp_day


# city_name = input('Give me a city: ')
# findcitylines(city_name)
