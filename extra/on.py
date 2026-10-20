import discord
from client import bot

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "help" in message.content.lower():
        await message.channel.send(f"{message.author.mention}, For help create support ticket.")
    if "star" in message.content.lower():
        print("star triggered")
        try:
            await message.pin()
            print("maybe pinned")
        except Exception as e:
            print(e)
    await bot.process_commands(message)