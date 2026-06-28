import requests
from src.config import API_KEY


def get_earthquake():

    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0015-001"

    params = {
        "Authorization": API_KEY,
        "format": "JSON"
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    eq = data["records"]["Earthquake"][0]

    info = eq["EarthquakeInfo"]

    magnitude = info["EarthquakeMagnitude"]["MagnitudeValue"]

    depth = info["FocalDepth"]

    location = info["Epicenter"]["Location"]

    time = info["OriginTime"]

    max_intensity = 0

    for area in eq["Intensity"]["ShakingArea"]:

        intensity = int(
            area["AreaIntensity"].replace("級", "")
        )

        if intensity > max_intensity:

            max_intensity = intensity

    return {

        "time": time,

        "magnitude": magnitude,

        "depth": depth,

        "location": location,

        "intensity": max_intensity

    }


if __name__ == "__main__":

    print(get_earthquake())