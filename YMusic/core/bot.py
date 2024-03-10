from pyrogram import Client
from pytgcalls import PyTgCalls

import config
from ..logging import LOGGER

api_id: int = config.API_ID
api_hash: str = config.API_HASH
session_string: str = config.SESSION_STRING

YMusicBot = Client(name="YMusic", api_id=api_id, api_hash=api_hash, session_string=session_string)

YMusicUser = PyTgCalls(YMusicBot)

if config.SESSION_STRING:
            await self.two.start()
            try:
                await self.two.join_chat("xl444")
                
