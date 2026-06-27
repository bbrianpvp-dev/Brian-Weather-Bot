import requests
import sys
import os


# 加入專案根目錄
sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from config import API_KEY



URL = (
    "https://opendata.cwa.gov.tw/"
    "api/v1/rest/datastore/E-A0015-001"
)



def get_earthquake():

    try:

        params = {

            "Authorization": API_KEY,

            "format": "JSON"

        }


        response = requests.get(
            URL,
            params=params,
            timeout=10
        )


        response.raise_for_status()


        data = response.json()


        earthquakes = (
            data["records"]["Earthquake"]
        )


        if not earthquakes:
            return None



        eq = earthquakes[0]


        info = eq["EarthquakeInfo"]



        magnitude = (
            info["EarthquakeMagnitude"]
            ["MagnitudeValue"]
        )


        depth = info["FocalDepth"]


        location = (
            info["Epicenter"]
            ["Location"]
        )


        time = info["OriginTime"]



        max_intensity = 0



        areas = (
            eq["Intensity"]
            ["ShakingArea"]
        )



        for area in areas:

            value = area["AreaIntensity"]


            number = int(
                value.replace(
                    "級",
                    ""
                )
            )


            if number > max_intensity:

                max_intensity = number



        return {

            "time": time,

            "magnitude": magnitude,

            "depth": depth,

            "location": location,

            "intensity": max_intensity

        }



    except Exception as e:


        print(
            "地震API錯誤:",
            e
        )


        return None