from telethon import TelegramClient, events
import random
import asyncio

#Written by @FBI34
api_id = 26347623
api_hash = 'd207f370168822f4396f130955aa2c58'
admin = 6676039554
textcomment = ['کامنت اول']
is_bot_online = True

#Written by @FBI34
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=admin))
async def handle_private_messages(event):
    global is_bot_online, textcomment
    message = event.message.message

    if message.startswith('/comment on'):
        if not is_bot_online:
            is_bot_online = True
            await event.respond('🤖 ربات روشن شد!')
        else:
            await event.respond('🤖 ربات از قبل روشن است!')

    elif message.startswith('/comment off'):
        if is_bot_online:
            is_bot_online = False
            await event.respond('🤖 ربات خاموش شد!')
        else:
            await event.respond('🤖 ربات از قبل خاموش است!')

    elif message.startswith('/add_comment'):
        if len(message.split(" ", 1)) < 2:
            await event.reply("خطا! متن کامنت را وارد کنید. ❌")
            return
        new_comment = message.split(" ", 1)[1]
        textcomment.append(new_comment)
        await event.reply(f"کامنت '{new_comment}' به لیست اضافه شد! ✅")

    elif message.startswith('/remove_comment'):
        if len(message.split(" ", 1)) < 2:
            await event.reply("خطا! شماره کامنت را وارد کنید. ❌")
            return
        try:
            index_to_remove = int(message.split(" ", 1)[1])
            if 0 <= index_to_remove < len(textcomment):
                removed_comment = textcomment.pop(index_to_remove)
                await event.reply(f"کامنت '{removed_comment}' از لیست حذف شد! ❌")
            else:
                await event.reply("خطا! شماره کامنت نامعتبر است. ❌")
        except ValueError:
            await event.reply("خطا! شماره کامنت باید یک عدد صحیح باشد. ❌")

    elif message.startswith('/help'):
        help_text = (
            "/comment on - روشن کردن ربات\n"
            "/comment off - خاموش کردن ربات\n"
            "/add_comment [comment] - اضافه کردن کامنت\n"
            "/remove_comment [index] - حذف کامنت با شماره\n"
            "/list_comments - نمایش لیست کامنت ها"
        )
        await event.reply(help_text)

    elif message.startswith('/list_comments'):
        if textcomment:
            comments_list = "\n".join(f"{index}: {comment}" for index, comment in enumerate(textcomment))
            await event.reply(f"لیست کامنت های فعلی:\n{comments_list}")
        else:
            await event.reply("لیست کامنت ها خالی است. ❌")

@client.on(events.NewMessage)
async def handle_channel_messages(event):
    global is_bot_online
    if is_bot_online:
        try:
            msg = await client.get_discussion_message(event.chat_id, event.message.id)
            await msg.reply(random.choice(textcomment))
        except Exception as e:
            print(f"خطا در پردازش پیام کانال: {e}")

client.start()
client.run_until_disconnected()

#Written by @FBI34
