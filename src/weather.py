import requests

from config import API_KEY



URL = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"



def get_weather():

    try:

        params = {

            "Authorization": API_KEY,

            "format": "JSON",

            "locationName": "臺北市"

        }



        response = requests.get(

            URL,

            params=params,

            timeout=10

        )


        response.raise_for_status()



        data = response.json()



        location = (
            data["records"]
            ["location"][0]
        )



        result = {

            "location": location["locationName"]

        }



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



    except Exception as e:


        print(
            "天氣 API 錯誤:",
            e
        )


        return None