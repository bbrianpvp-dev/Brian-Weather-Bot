import requests
from config import API_KEY


def get_earthquake():

    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0015-001"


    params = {
        "Authorization": API_KEY,
        "format": "JSON"
    }


    response = requests.get(url, params=params)

    data = response.json()


    eq = data["records"]["Earthquake"][0]


    info = eq["EarthquakeInfo"]


    magnitude = info["EarthquakeMagnitude"]["MagnitudeValue"]

    depth = info["FocalDepth"]

    location = info["Epicenter"]["Location"]

    time = info["OriginTime"]



    # 最大震度

    max_intensity = 0


    areas = eq["Intensity"]["ShakingArea"]


    for area in areas:

        value = area["AreaIntensity"]

        number = int(value.replace("級",""))

        if number > max_intensity:
            max_intensity = number



    return {

        "time": time,

        "magnitude": magnitude,

        "depth": depth,

        "location": location,

        "intensity": max_intensity

    }