from weather import get_weather
from earthquake import get_earthquake


print("🌤️ Brian Weather Bot")


weather = get_weather()


print()
print("📍", weather["city"])
print("☁️ 天氣:", weather["weather"])
print("☔ 降雨機率:", weather["rain"], "%")
print("🌡️ 最低溫:", weather["min_temp"], "°C")
print("🌡️ 最高溫:", weather["max_temp"], "°C")

earthquake = get_earthquake()

print()

print("🚨 地震速報")

print("時間:", earthquake["time"])
print("規模:", earthquake["magnitude"])
print("深度:", earthquake["depth"], "km")
print("位置:", earthquake["location"])