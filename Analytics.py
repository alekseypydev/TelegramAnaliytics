# 
# Telegram Analytics 
# 
# by @AlekseyForWork
#
# Telegram Channel - t.me/AlekseyDevelop

from pyrogram import Client

api_id =  
api_hash = "" 
session_name = 'userbot'

with Client(session_name, api_id, api_hash) as app:
    dialogs = app.get_dialogs()

    chats_count = 0
    lchats_count = 0
    groups_count = 0
    channels_count = 0
    bots_count = 0
    for dialog in dialogs:
        chat = dialog.chat
        chats_count += 1
        if str(chat.type) == 'ChatType.PRIVATE':
            lchats_count += 1

        elif str(chat.type) == 'ChatType.SUPERGROUP' or str(chat.type) == 'ChatType.GROUP':
            groups_count += 1

        elif str(chat.type) == 'ChatType.CHANNEL':
            channels_count += 1

        elif str(chat.type) == 'ChatType.BOT':
            bots_count += 1




    print('Всего чатов: ' + str(chats_count))
    print('Личных чатов: ' + str(lchats_count))
    print('Групп: ' + str(groups_count))
    print('Каналов: ' + str(channels_count))
    print('Ботов: ' + str(bots_count))
