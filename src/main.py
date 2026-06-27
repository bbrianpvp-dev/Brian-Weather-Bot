from weather import get_weather
from earthquake import get_earthquake


print("🌤️ Brian Weather Bot\n")


# 天氣

weather = get_weather()


print("📍", weather["location"])
print("☁️ 天氣:", weather["weather"])
print("☔ 降雨機率:", weather["rain"], "%")
print("🌡️ 最低溫:", weather["min_temp"], "°C")
print("🌡️ 最高溫:", weather["max_temp"], "°C")



# 地震

earthquake = get_earthquake()


if earthquake:

    print("\n🚨 地震速報")

    print("時間:", earthquake["time"])
    print("規模:", earthquake["magnitude"])
    print("深度:", earthquake["depth"], "km")
    print("位置:", earthquake["location"])


    if earthquake["intensity"] >= 2:

        print("⚠️ 地震警報：達到2級以上")
