from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from filters import command
from YMusic import app
from YMusic.utils.queue import clear_queue
from YMusic.utils.loop import get_loop, set_loop
from YMusic.core import userbot
from YMusic.misc import SUDOERS
import config

STOP_COMMAND = ["كافي", "ايقاف"]

PAUSE_COMMAND = ["مؤقت"]

RESUME_COMMAND = ["استمرار"]

MUTE_COMMAND = ["كتم"]

UNMUTE_COMMAND = ["رفع"]

VOLUME_COMMAND = ["ضبط", "اضبط"]

LOOP_COMMAND = ["تكرار"]

LOOPEND_COMMAND = ["انهاء"]



@app.on_message(command(STOP_COMMAND))
async def _stop(_, message):
    # Get administrators
    administrators = []
    async for m in app.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m)
    if (message.from_user.id) in SUDOERS or (message.from_user.id) in [admin.user.id for admin in administrators]:
        Text = await userbot.stop(message.chat.id)
        try:
            clear_queue(message.chat.id)
        except:
            pass
        await message.reply_text(Text)
    else:
        return await message.reply_text("-› ماعنـدك صـلاحيـات تـرى .")


@app.on_message(command(STOP_COMMAND))
async def _stop(_, message):
    if (len(message.command)) != 2:
        await message.reply_text("-› الامـر خطا .")
    else:
        msg_id = msg_id = message.text.split(" ", 1)[1]
        Text = await userbot.stop(msg_id)
        await message.reply_text(Text)

@app.on_message(command(PAUSE_COMMAND)
)
async def _pause(_, message):
    # Get administrators
    administrators = []
    async for m in app.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m)
    if (message.from_user.id) in SUDOERS or (message.from_user.id) in [admin.user.id for admin in administrators]:
        Text = await userbot.pause(message.chat.id)
        await message.reply_text(Text)
    else:
        return await message.reply_text("-› ماعنـدك صـلاحيـات تـرى .")


@app.on_message(command(PAUSE_COMMAND)
)
async def _pause(_, message):
    if (len(message.command)) != 2:
        await message.reply_text("-› الأمـر خطـا .")
    else:
        msg_id = msg_id = message.text.split(" ", 1)[1]
        Text = await userbot.pause(msg_id)
        await message.reply_text(Text)


@app.on_message(command(RESUME_COMMAND)
)
async def _resume(_, message):
    # Get administrators
    administrators = []
    async for m in app.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m)
    if (message.from_user.id) in SUDOERS or (message.from_user.id) in [admin.user.id for admin in administrators]:
        Text = await userbot.resume(message.chat.id)
        await message.reply_text(Text)
    else:
        return await message.reply_text("-› ماعنـدك صـلاحيـات تـرى .")


@app.on_message(command(RESUME_COMMAND)
)
async def _resume(_, message):
    if (len(message.command)) != 2:
        await message.reply_text("-› الأمـر خطـا .")
    else:
        msg_id = msg_id = message.text.split(" ", 1)[1]
        Text = await userbot.resume(msg_id)
        await message.reply_text(Text)


@app.on_message(command(MUTE_COMMAND)
)
async def _mute(_, message):
    if message.from_user and message.from_user.is_self:
        reply = message.edit
    else:
        reply = message.reply_text
    Text = await userbot.mute(message.chat.id)
    await reply(Text)


@app.on_message(command(MUTE_COMMAND)
)
async def _mute(_, message):
    if (len(message.command)) != 2:
        await message.reply_text("-› الأمـر خطـا .")
    else:
        msg_id = msg_id = message.text.split(" ", 1)[1]
        Text = await userbot.mute(msg_id)
        await message.reply_text(Text)


@app.on_message(command(UNMUTE_COMMAND)
)
async def _unmute(_, message):
    Text = await userbot.unmute(message.chat.id)
    await message.reply_text(Text)


@app.on_message(command(UNMUTE_COMMAND)
)
async def _unmute(_, message):
    if (len(message.command)) != 2:
        await message.reply_text("-› الأمـر خطـا .")
    else:
        msg_id = msg_id = message.text.split(" ", 1)[1]
        Text = await userbot.unmute(msg_id)
        await message.reply_text(Text)


@app.on_message(command(VOLUME_COMMAND)
)
async def _volume(_, message):
    try:
        vol = int(message.text.split()[1])
        Text = await userbot.changeVolume(message.chat.id, vol)
    except:
        Text = await userbot.changeVolume(message.chat.id)
    await message.reply_text(Text)


@app.on_message(command(LOOP_COMMAND)
)
async def _loop(_, message):
    # Get administrators
    administrators = []
    async for m in app.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m)
    if (message.from_user.id) in SUDOERS or (message.from_user.id) in [admin.user.id for admin in administrators]:
        loop = await get_loop(message.chat.id)
        if loop == 0:
            try:
                await set_loop(message.chat.id, 10000)
                await message.reply_text("-› تم تفعـيل التكـرار سيتـم 10000 مرات .")
            except Exception as e:
                return await message.reply_text(f"Error:- <code>{e}</code>")

        else:
            await message.reply_text("-› تم تفعـيل التكـرار بالفـعل .")
    else:
        return await message.reply_text("-› ماعنـدك صـلاحيـات تـرى .")


@app.on_message(command(LOOPEND_COMMAND)
)
async def _endLoop(_, message):
    # Get administrators
    administrators = []
    async for m in app.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m)
    if (message.from_user.id) in SUDOERS or (message.from_user.id) in [admin.user.id for admin in administrators]:
        loop = await get_loop(message.chat.id)
        if loop == 0:
            await message.reply_text("-› لم يتـم التكـرار .")
        else:
            try:
                await set_loop(message.chat.id, 0)
                await message.reply_text("-› معطلـة .")
            except Exception as e:
                return await message.reply_text(f"Error:- <code>{e}</code>")
    else:
        return await message.reply_text("-› ماعنـدك صـلاحيـات تـرى .")
        
