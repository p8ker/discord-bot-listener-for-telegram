import disnake
import telebot

#varieble for telegram bot
botg = telebot.TeleBot("TOKEN TELEGRAM", parse_mode=None)

#varieble for discord bot
intents = disnake.Intents.all()
botds = disnake.Client(intents=intents)

#discord event reading user message 
@botds.event
async def on_message(message: disnake.Message):
    if message.author.bot:
        return
    if message.content:
        #telegram bot write message user 
        botg.send_message(text=f"{message.author.name}:\n{message.content}", chat_id=-1002171931218)#chat_id - its id group or channel

#run bots
botds.run('TOKEN DISCORD')

botg.infinity_polling()