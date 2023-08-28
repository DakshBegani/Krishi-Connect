from geopy.geocoders import Nominatim
import requests
from .date_formatter import format_date
 
geolocator = Nominatim(user_agent="geoapiExercises")

def weather_data(zipcode):
    location = geolocator.geocode(zipcode)

    result = location.raw["display_name"]
    items = result.split(", ")

    location_data = {
        "city": items[0],
        "district": items[1],
        "state": items[2],
        "pin_code": items[3],
        "country": items[4],
        "lat": str(location.latitude),
        "lon": str(location.longitude)
    }
    base_url_weatherbit = "https://api.weatherbit.io/v2.0/forecast/agweather?"
    api_key_weatherbit = "d725b3fd6830440badb45493db1a3ff1"
    api_url_weatherbit = base_url_weatherbit + "lat=" + location_data["lat"] + "&lon=" + location_data["lon"] + "&key=" + api_key_weatherbit

    weather_forecast = requests.get(api_url_weatherbit)
    x = weather_forecast.json()['data']
    # print(x)

    weather_data = {
        "city": items[0],
        "district": items[1],
        "state": items[2],
        "pin_code": items[3],
        "country": items[4],
        "lat": str(location.latitude),
        "lon": str(location.longitude)
    }
    weather_list = []
    for i in x:
        date = format_date(i['valid_date'])
        weather_dict = {
            'date': date,
            'temps': [i['skin_temp_max'], i['skin_temp_avg'], i['skin_temp_min']],
            'precip': i['precip'],
            'humidity': i['specific_humidity'],
            'soil_moisture': i['soilm_10_40cm'],
            'wind_speed': i['wind_10m_spd_avg']
        }
        weather_list.append(weather_dict)
    print(weather_list)
    return weather_list
# valid_date:
# precip
# skin_temp_avg
# specific_humidity:
# soilm_0_10cm:
# wind_10m_spd_avg