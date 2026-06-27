from weather import get_weather


print("🌤️ Brian Weather Bot")


weather = get_weather()


print()
print("📍", weather["city"])
print("☁️ 天氣:", weather["weather"])
print("☔ 降雨機率:", weather["rain"], "%")
print("🌡️ 最低溫:", weather["min_temp"], "°C")
print("🌡️ 最高溫:", weather["max_temp"], "°C")