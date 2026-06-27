from weather import get_weather


print("🌤️ Brian Weather Bot 啟動成功！")

data = get_weather()

print("地點:", data["city"])
print("溫度:", data["temperature"], "°C")
print("天氣:", data["condition"])
print("降雨機率:", data["rain"], "%")