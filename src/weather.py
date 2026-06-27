import requests
from config import API_KEY


def get_weather():

    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"

    params = {
        "Authorization": API_KEY,
        "format": "JSON",
        "locationName": "臺北市"
    }


    response = requests.get(
        url,
        params=params
    )


    data = response.json()


    location = data["records"]["location"][0]


    result = {}

    result["location"] = location["locationName"]


    weather = location["weatherElement"]


    for element in weather:

        name = element["elementName"]


        if name == "Wx":
            result["weather"] = (
                element["time"][0]
                ["parameter"]
                ["parameterName"]
            )


        elif name == "PoP":
            result["rain"] = (
                element["time"][0]
                ["parameter"]
                ["parameterName"]
            )


        elif name == "MinT":
            result["min_temp"] = (
                element["time"][0]
                ["parameter"]
                ["parameterName"]
            )


        elif name == "MaxT":
            result["max_temp"] = (
                element["time"][0]
                ["parameter"]
                ["parameterName"]
            )


    return result