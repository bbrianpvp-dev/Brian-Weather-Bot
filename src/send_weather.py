import asyncio

from src.weather import get_weather
from src.discord_utils import send_message


def create_weather_message(data):

    message = f"""
🌤️ **Brian Weather Bot**

📍 地點：
{data['location']}

☁️ 天氣：
{data['weather']}

☔ 降雨機率：
{data['rain']} %

🌡️ 溫度：
{data['min_temp']}°C ～ {data['max_temp']}°C

🕖 每日天氣通知
"""

    return message



async def main():

    weather = get_weather()

    message = create_weather_message(
        weather
    )

    await send_message(
        message
    )


if __name__ == "__main__":

    asyncio.run(main())