import discord
from discord.ext import commands, tasks

from datetime import datetime

import config

from earthquake import get_earthquake
from weather import get_weather



# =====================
# Discord 設定
# =====================

intents = discord.Intents.default()


bot = commands.Bot(
    command_prefix="!",
    intents=intents
)



# =====================
# 防重複紀錄
# =====================

last_earthquake_time = None

last_weather_date = None



# =====================
# 地震監控
# =====================

@tasks.loop(seconds=60)
async def earthquake_monitor():

    global last_earthquake_time


    earthquake = get_earthquake()


    if earthquake is None:

        print("無地震資料")

        return



    earthquake_time = earthquake["time"]



    # 同一筆地震跳過

    if earthquake_time == last_earthquake_time:

        print(
            "同一筆地震，跳過"
        )

        return



    last_earthquake_time = earthquake_time



    intensity = earthquake["intensity"]



    print(
        f"偵測地震 最大震度:{intensity}"
    )



    # =====================
    # 震度 >= 2 通知
    # =====================

    if intensity >= 2:


        user = await bot.fetch_user(
            config.USER_ID
        )



        embed = discord.Embed(

            title="🚨 地震速報",

            description="中央氣象署地震資料",

            color=0xff0000

        )


        embed.add_field(

            name="📍 位置",

            value=earthquake["location"],

            inline=False

        )


        embed.add_field(

            name="📏 規模",

            value=str(
                earthquake["magnitude"]
            ),

            inline=True

        )


        embed.add_field(

            name="🌊 深度",

            value=f'{earthquake["depth"]} km',

            inline=True

        )


        embed.add_field(

            name="⚠️ 最大震度",

            value=f'{earthquake["intensity"]}級',

            inline=True

        )


        embed.add_field(

            name="🕒 時間",

            value=earthquake["time"],

            inline=False

        )


        embed.set_footer(

            text="Brian Weather Bot 🚨"

        )



        await user.send(

            embed=embed

        )


        print(
            "地震通知完成"
        )



    else:

        print(
            "震度小於2級，不通知"
        )





# =====================
# 每日天氣通知
# =====================

@tasks.loop(minutes=1)
async def daily_weather():

    global last_weather_date



    now = datetime.now()



    # 早上7點

    if now.hour == 7 and now.minute == 0:



        today = now.date()



        # 今天已通知

        if today == last_weather_date:

            return



        weather = get_weather()



        if weather is None:

            print(
                "天氣資料取得失敗"
            )

            return



        last_weather_date = today



        user = await bot.fetch_user(

            config.USER_ID

        )



        embed = discord.Embed(

            title="🌤️ 今日天氣",

            description="中央氣象署資料",

            color=0x00aaff

        )



        embed.add_field(

            name="📍 地點",

            value=weather["location"],

            inline=False

        )



        embed.add_field(

            name="☁️ 天氣",

            value=weather["weather"],

            inline=False

        )


        embed.add_field(

            name="🌡️ 溫度",

            value=(
                f'{weather["min_temp"]}°C'
                f' ~ '
                f'{weather["max_temp"]}°C'
            ),

            inline=True

        )



        embed.add_field(

            name="☔ 降雨機率",

            value=f'{weather["rain"]}%',

            inline=True

        )


        embed.set_footer(

            text="Brian Weather Bot 🌤️"

        )



        await user.send(

            embed=embed

        )


        print(
            "每日天氣通知完成"
        )





# =====================
# Bot 啟動
# =====================

@bot.event
async def on_ready():


    print(
        f"登入成功: {bot.user}"
    )



    user = await bot.fetch_user(

        config.USER_ID

    )



    await user.send(

        "🌤️ Brian Weather Bot 啟動成功！\n"
        "🚨 地震監控已啟動\n"
        "🌤️ 每日07:00天氣通知已啟動"

    )



    if not earthquake_monitor.is_running():

        earthquake_monitor.start()



    if not daily_weather.is_running():

        daily_weather.start()



# =====================
# 啟動
# =====================

bot.run(

    config.BOT_TOKEN

)