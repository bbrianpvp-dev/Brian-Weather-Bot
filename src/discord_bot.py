import discord
from discord.ext import commands, tasks

import config

from earthquake import get_earthquake


# =====================
# Discord 設定
# =====================

intents = discord.Intents.default()


bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# =====================
# 防止重複通知
# =====================

last_earthquake_time = None



# =====================
# 地震監控
# =====================

@tasks.loop(seconds=60)
async def earthquake_monitor():

    global last_earthquake_time


    user = await bot.fetch_user(
        config.USER_ID
    )


    earthquake = get_earthquake()


    if earthquake is None:

        print("目前沒有地震資料")

        return



    time = earthquake["time"]

    intensity = earthquake["intensity"]



    # 同一筆地震跳過

    if time == last_earthquake_time:

        print(
            "同一筆地震，跳過通知"
        )

        return



    # 更新最新時間

    last_earthquake_time = time



    print(
        f"偵測地震 最大震度:{intensity}"
    )



    # =====================
    # 震度 >= 2 才通知
    # =====================

    if intensity >= 2:


        message = f"""
🚨 地震警報

🕒 時間:
{earthquake["time"]}

📏 規模:
{earthquake["magnitude"]}

🌊 深度:
{earthquake["depth"]} km

📍 位置:
{earthquake["location"]}

⚠️ 最大震度:
{earthquake["intensity"]}級
"""


        await user.send(
            message
        )


        print(
            "已發送地震通知"
        )


    else:


        print(
            "震度小於2級，不通知"
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
        "🚨 地震監控已開始\n"
        "📢 震度2級以上會通知"
    )


    print(
        "啟動通知完成"
    )


    if not earthquake_monitor.is_running():

        earthquake_monitor.start()



# =====================
# 啟動 Bot
# =====================

bot.run(
    config.BOT_TOKEN
)