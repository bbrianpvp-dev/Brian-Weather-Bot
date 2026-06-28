import asyncio
import json
import os


from src.earthquake import get_earthquake
from src.discord_utils import send_message



LAST_FILE = "last_earthquake.json"



def load_last():

    if not os.path.exists(LAST_FILE):

        return None


    with open(
        LAST_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_last(data):

    with open(
        LAST_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def create_message(eq):

    message = f"""
🚨 **地震警報**

🕒 時間：
{eq['time']}

📍 位置：
{eq['location']}

📏 規模：
{eq['magnitude']}

⬇️ 深度：
{eq['depth']} km

🌊 最大震度：
{eq['intensity']} 級

⚠️ 已達通知標準
"""

    return message



async def main():

    earthquake = get_earthquake()


    # 震度小於2，不通知

    if earthquake["intensity"] < 2:

        print(
            "震度不足，不通知"
        )

        return



    last = load_last()



    # 避免重複通知

    if last:

        if (
            last["time"]
            ==
            earthquake["time"]
        ):

            print(
                "已通知過此地震"
            )

            return



    message = create_message(
        earthquake
    )


    await send_message(
        message
    )


    save_last(
        earthquake
    )


    print(
        "地震通知完成"
    )



if __name__ == "__main__":

    asyncio.run(main())