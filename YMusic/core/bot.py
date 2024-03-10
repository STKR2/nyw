from pyrogram import Client
from pytgcalls import PyTgCalls
import sys
import config
from YMusic.core import bot
from ..logging import LOGGER

api_id: int = config.API_ID
api_hash: str = config.API_HASH
session_string: str = config.SESSION_STRING

YMusicBot = Client(name="YMusic", api_id=api_id, api_hash=api_hash, session_string=session_string)

YMusicUser = PyTgCalls(YMusicBot)

   my_bot = bot()
await my_bot.start()
try:
    await my_bot.join_chat("xl444")
    assistants.append(2)
    await my_bot.send_message(config.LOG_GROUP_ID, "- تم التشغيل .")
except Exception as e:
    print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main_function())
