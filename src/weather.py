import requests
from src.config import API_KEY


def get_weather(city="臺北市"):

    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"

    params = {
        "Authorization": API_KEY,
        "format": "JSON",
        "locationName": city
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    location = data["records"]["location"][0]

    result = {
        "location": location["locationName"]
    }

    for element in location["weatherElement"]:

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


if __name__ == "__main__":

    weather = get_weather()

    print(weather)