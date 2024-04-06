from pyrogram import Client, filters
from pyrogram.types import Message
import random, os
import asyncio

app = Client(
    name='self', # session name
    api_id=26347623, # api id
    api_hash='d207f370168822f4396f130955aa2c58' # api hash
)
admin = 6676039554 # admin id
textcomment = ['کامنت اول'] # comments
is_bot_online = True

@app.on_message(filters.channel)
async def comment(c: Client, m: Message) :
    if is_bot_online:
        try:
            msg = await app.get_discussion_message(m.chat.id, m.id)
        finally:
            await msg.reply(random.choice(textcomment))

@app.on_message(filters.private & filters.user(admin) & filters.command("add_comment"))
async def add_comment(c: Client, m: Message):
    global textcomment
    new_comment = m.text.split(" ", 1)[1]
    textcomment.append(new_comment)
    await m.reply(f"Comment '{new_comment}' has been added to the list!")

@app.on_message(filters.private & filters.user(admin) & filters.command("remove_comment"))
async def remove_comment(c: Client, m: Message):
    global textcomment
    index_to_remove = int(m.text.split(" ", 1)[1])
    if 0 <= index_to_remove < len(textcomment):
        removed_comment = textcomment.pop(index_to_remove)
        await m.reply(f"Comment '{removed_comment}' was removed from the list!")
    else:
        await m.reply("EROR")

@app.on_message(filters.private & filters.user(admin) & filters.command("start"))
async def start_bot(c: Client, m: Message):
    global is_bot_online
    if not is_bot_online:
        is_bot_online = True
        await m.reply("on bot")

@app.on_message(filters.private & filters.user(admin) & filters.command("stop"))
async def stop_bot(c: Client, m: Message):
    global is_bot_online
    if is_bot_online:
        is_bot_online = False
        await m.reply("off bot")

app.run()

#Written by @FBI34