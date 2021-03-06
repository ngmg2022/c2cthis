import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

# start the bot
print("Starting...")
try:
    apiid = config("APP_ID", cast=int)
    apihash = config("API_HASH")
    bottoken = config("BOT_TOKEN")
    frm = config("FROM_CHANNEL", cast=int)
    tochnl = config("TO_CHANNEL", cast=int)
    tochnl2 =config("TO_CHANNEL2",cast=int)
    datgbot = TelegramClient('bot', apiid, apihash).start(bot_token=bottoken)
except:
    print("Environment vars are missing! Kindly recheck.")
    print("Bot is quiting...")
    exit()


@datgbot.on(events.NewMessage(pattern="/start"))
async def _(event):
    ok = await datgbot(GetFullUserRequest(event.sender_id))
    await event.reply(f"π·π ππ`{ok.user.first_name}`!\n\nπΈ ππ π π²ππππππ πΏπππππ πππ. πΏππππ /help ππ πππ ππππ \n\nI can be used in only two channels (one user) at a time..\n\n[π€](https://telegra.ph/file/1eca514b5e6202b1d92b3.jpg)", 
    buttons=[Button.url("π€Main Groupπ°οΈ", url="t.me/danuma01"), Button.url("πBot NewsπΈ", url="https://t.me/dbotai"), Button.url("βοΈDeveloperβοΈ", url="https://lasiya.ml")], link_preview=True)


@datgbot.on(events.NewMessage(pattern="/help"))
async def helpp(event):
    await event.reply("**Help**\n\nThis bot will send all new posts in one channel to the other channel (without forwarded tag).\nIt can be used only in two channels at a time, \n\nAdd me to both the channels and make me an admin in both, and all new messages would be autoposted on the linked channel!\n\nLiked the bot? Drop a β₯ to Danuma project")

@datgbot.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event): 
    if not event.is_private:
        try:
            await event.client.send_message(tochnl,tochnl2,event.message)
        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")


print("Bot has started.")
print("Visit @Danuma01")
datgbot.run_until_disconnected()
