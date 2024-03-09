from YMusic import app
from YMusic.core import userbot
from YMusic.utils import ytDetails
from YMusic.utils.queue import QUEUE, add_to_queue
from YMusic.misc import SUDOERS
from filters import command
from pyrogram import filters

import asyncio
import random
import time

import config

PLAY_COMMAND = ["تشغيل", "شغل"]

async def ytdl(format: str, link: str):
    stdout, stderr = await bash(f'yt-dlp --geo-bypass -g -f "[height<=?720][width<=?1280]" {link}')
    if stdout:
        return 1, stdout
    return 0, stderr


async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err


async def processReplyToMessage(message):
    msg = message.reply_to_message
    if msg.audio or msg.voice:
        m = await message.reply_text("𓏺-› جاري التشغيل .")
        audio_original = await msg.download()
        input_filename = audio_original
        return input_filename, m
    else:
        return None


async def playWithLinks(link):
    if "&" in link:
        pass
    if "?" in link:
        pass

    return 0


@app.on_message(command(PLAY_COMMAND)  
)
async def _aPlay(_, message):
    start_time = time.time()
    chat_id = message.chat.id
    if (message.reply_to_message) is not None:
        if message.reply_to_message.audio or message.reply_to_message.voice:
            input_filename, m = await processReplyToMessage(message)
            if input_filename is None:
                await message.reply_text("-› رد على ملـف صـوتي أو شـي للبـحث .")
                return
            await m.edit("-› سيتـم التشـغيل الآن .")
            Status, Text = await userbot.playAudio(chat_id, input_filename)
            if Status == False:
                await m.edit(Text)
            else:
                if chat_id in QUEUE:
                    queue_num = add_to_queue(
                        chat_id, message.reply_to_message.audio.title[:19], message.reply_to_message.audio.duration, message.reply_to_message.audio.file_id, message.reply_to_message.link)
                    await m.edit(f"-› {queue_num}\n{message.reply_to_message.audio.title[:19]}\nTera gaana queue me daal diya hu")
                    return
                finish_time = time.time()
                total_time_taken = str(int(finish_time - start_time)) + " ثانيـة "
                await m.edit(f"-› تم التشـغيل بنجـاح .\n\n𓏺-› اسم المـلف : [{message.reply_to_message.audio.title[:19]}]({message.reply_to_message.link})\n𓏺-› وقـت المـلف : {message.reply_to_message.audio.duration}\n𓏺-› انتَ تدري شغـلتها خـلال : {total_time_taken}", disable_web_page_preview=True)
    elif (len(message.command)) < 2:
        await message.reply_text("-› الامـر غلـط ترى .")
    else:
        m = await message.reply_text("-› تم البُـحث .")
        query = message.text.split(" ", 1)[1]
        try:
            title, duration, link = ytDetails.searchYt(query)
        except Exception as e:
            await message.reply_text(f"Error:- <code>{e}</code>")
            return
        await m.edit("-› جـاري التشغـيل .")
        format = "bestaudio"
        resp, songlink = await ytdl(format, link)
        if resp == 0:
            await m.edit(f"❌ yt-dl issues detected\n\n» `{songlink}`")
        else:
            if chat_id in QUEUE:
                queue_num = add_to_queue(
                    chat_id, title[:19], duration, songlink, link)
                await m.edit(f"-› {queue_num}\n{title[:19]}\n-› تم الأضـافة بنجـاح .")
                return
            # await asyncio.sleep(1)
            Status, Text = await userbot.playAudio(chat_id, songlink)
            if Status == False:
                await m.edit(Text)
            else:
                if duration is None:
                    duration = "Playing From LiveStream"
                add_to_queue(chat_id, title[:19], duration, songlink, link)
                finish_time = time.time()
                total_time_taken = str(int(finish_time - start_time)) + "ثانيـةة"
                await m.edit(f"-› تم التشـغيل بنجـاح .\n\n𓏺-› اسم المـلف : [{title[:19]}]({link}) \n-› وقـت المـلف : {duration} \n𓏺-› انتَ تدري شغـلتها خـلال : {total_time_taken} ", disable_web_page_preview=True)


@app.on_message(command(PLAY_COMMAND) & SUDOERS)
async def _raPlay(_, message):
    start_time = time.time()
    if (message.reply_to_message) is not None:
        await message.reply_text("-› خـطأ .")
    elif (len(message.command)) < 3:
        await message.reply_text("-› الأمـر خـطأ .")
    else:
        m = await message.reply_text("-› التحميـل .")
        query = message.text.split(" ", 2)[2]
        msg_id = message.text.split(" ", 2)[1]
        title, duration, link = ytDetails.searchYt(query)
        await m.edit("-› يجـري التحميـل .")
        format = "bestaudio"
        resp, songlink = await ytdl(format, link)
        if resp == 0:
            await m.edit(f"❌ yt-dl issues detected\n\n» `{songlink}`")
        else:
            Status, Text = await userbot.playAudio(msg_id, songlink)
            if Status == False:
                await m.edit(Text)
            else:
                if duration is None:
                    duration = "Playing From LiveStream"
                finish_time = time.time()
                total_time_taken = str(int(finish_time - start_time)) + " ثانيـة "
                await m.edit(f"-› تم التشـغيل بنجـاح .\n\n𓏺-› اسم المـلف : [{title[:19]}]({link})\n-› وقـت المـلف : {duration}\n-› انتَ تـدري شغلتـها خـلال : {total_time_taken}", disable_web_page_preview=True)
