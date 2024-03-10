import asyncio
import math
import os
import time
import httpx
import aiofiles
import aiohttp
from urllib.parse import urlparse
from filters import command
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from YMusic import app

if not os.path.exists("downloads"):
    os.makedirs("downloads")

@app.on_message(command(["بحث", "يوت"]))
async def song(client, message: Message):
    urlissed = get_text(message)
    if not urlissed:
        await client.send_message(
            message.chat.id,
            "صيغة الأمر غير صالحة يرجى مراجعة قائمة التعليمات لمعرفة المزيد!",
        )
        return
    pablo = await client.send_message(message.chat.id, f"** جاري البحث** `{urlissed}`")
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    mio[0]["duration"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    async with httpx.AsyncClient() as client_httpx:
        response = await client_httpx.get(kekme)
        with open("downloads/hqdefault.jpg", "wb") as img_file:
            img_file.write(response.content)
        sedlyf = "downloads/hqdefault.jpg"
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "240",
                }
            ],
            "outtmpl": "downloads/%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(mo, download=True)
    except Exception as e:
        await pablo.edit(f"**قدم للتحميل** \n**خطاء :** `{str(e)}`")
        return
    c_time = time.time()
    file_stark = f"downloads/{ytdl_data['id']}.mp3"
    capy = f"""
**🏷️ اسم الاغنية:** [{thum}]({mo})
**🎧 طلب من العزيز:** {message.from_user.mention}
"""
    await client.send_audio(
        message.chat.id,
        audio=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        title=str(ytdl_data["title"]),
        performer=str(ytdl_data["uploader"]),
        thumb=sedlyf,
        caption=capy,
        progress=progress,
        progress_args=(
            pablo,
            c_time,
            f"**📥 جاري التنزيل** `{urlissed}`",
            file_stark,
        ),
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)
