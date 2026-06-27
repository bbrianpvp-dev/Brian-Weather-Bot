import discord
from discord.ext import commands

import config


intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():

    print(f"登入成功: {bot.user}")

    try:
        user = await bot.fetch_user(config.USER_ID)

        await user.send(
            "🌤️ Brian Weather Bot 啟動成功！"
        )

        print("DM 發送成功")

    except discord.Forbidden:
        print("DM 失敗：Discord 禁止傳送私人訊息")

    except Exception as e:
        print("錯誤:", e)


bot.run(config.BOT_TOKEN)