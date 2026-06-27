import requests
from config import API_KEY


def get_weather():

    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-063"

    params = {
        "Authorization": API_KEY,
        "format": "JSON",
        "locationName": "臺北市"
    }


    response = requests.get(url, params=params)

    data = response.json()


    location = data["records"]["Locations"][0]["Location"][0]


    weather_elements = location["WeatherElement"]


    result = {
        "location": "臺北市",
        "weather": "",
        "rain": "",
        "min_temp": "",
        "max_temp": ""
    }


    for element in weather_elements:

        name = element["ElementName"]


        if name == "天氣現象":
            result["weather"] = element["Time"][0]["ElementValue"][0]["Weather"]


        elif name == "降雨機率":
            result["rain"] = element["Time"][0]["ElementValue"][0]["ProbabilityOfPrecipitation"]


        elif name == "最低溫度":
            result["min_temp"] = element["Time"][0]["ElementValue"][0]["MinTemperature"]


        elif name == "最高溫度":
            result["max_temp"] = element["Time"][0]["ElementValue"][0]["MaxTemperature"]


    return result