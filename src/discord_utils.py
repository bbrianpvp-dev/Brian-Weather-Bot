import discord
from src.config import BOT_TOKEN, USER_ID


class BrianDiscordBot(discord.Client):

    async def on_ready(self):

        print(f"登入成功：{self.user}")


async def send_message(message):

    intents = discord.Intents.default()

    client = BrianDiscordBot(
        intents=intents
    )

    @client.event
    async def on_ready():

        user = await client.fetch_user(USER_ID)

        await user.send(message)

        print("DM 發送成功")

        await client.close()

    await client.start(BOT_TOKEN)