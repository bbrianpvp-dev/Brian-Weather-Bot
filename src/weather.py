import requests
from config import API_KEY


def get_weather():

    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"

    params = {
        "Authorization": API_KEY,
        "format": "JSON",
        "locationName": "臺北市"
    }

    response = requests.get(url, params=params)

    data = response.json()


    location = data["records"]["location"][0]

    city = location["locationName"]


    weather = location["weatherElement"]


    result = {
        "city": city
    }


    for item in weather:

        name = item["elementName"]

        value = item["time"][0]["parameter"]["parameterName"]


        if name == "Wx":
            result["weather"] = value

        elif name == "PoP":
            result["rain"] = value

        elif name == "MinT":
            result["min_temp"] = value

        elif name == "MaxT":
            result["max_temp"] = value


    return result