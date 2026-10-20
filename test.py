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
    

@bot.tree.command(name="greet", description="greets ypu")
async def greet(interaction: discord.Interaction):
    print("DEBUG: /greet ran by user")
    user = interaction.user.mention
    await interaction.response.send_message(f"Assalamu Alaikum {user}")

@bot.tree.command(name="star", description="piins a meassgae.")
@app_commands.describe(msg_id="msg id")
async def star(interaction: discord.Interaction, msg_id: str):
    await interaction.response.defer(thinking=True)
    message_id = int(msg_id.strip())

    
    try:
        msg = await interaction.channel.fetch_message(message_id)
        await msg.pin()
        await interaction.followup.send("pinned")
    except Exception as e:
        await interaction.followup.send(e)
    except ValueError:
        await interaction.followup.send("Invalid id")
    except discord.NotFound:
        await interaction.followup.send("msg not found")
    except discord.Forbidden:
        await interaction.followup.send("bot has no permission")


# @bot.tree.command(name="play", description="plays a music")
# @applciation.describe(song_query="Search song")
# async def play(interaction: discord.interaction, song_query: str):
#     await interaction.response.defer()
#     vc = interaction.user.voice.channel
#     
#     v_client = interaction.guild.voice.client
#     if v_client is None:
#         v_client = await vc.channel.connect
# 
#         ydl_options = {
#             "format"="bestaudio[abr<=96]/bestaudio",
#             "noplaylist" = True,
#             "youtube_include_dash_format" = False,
#             "youtube_include_dash_format" = False,
#         }
# 
#         query = "ytsearch1: " + song_query


message_queue = queue.Queue()
pin_queue = queue.Queue()
@tasks.loop(seconds=0.5)
async def send_core():
    try:
        cid, msg = message_queue.get_nowait()
        channel = bot.get_channel(int(cid))
        await channel.send(msg)
    except queue.Empty:
        pass
    except Exception as e:
        print(f"\n{e}")

@tasks.loop(seconds=0.5)
async def pin_core():
    try:
        cid, msgid = pin_queue.get_nowait()
        msgidd = await bot.get_message(msg_id)
        channel = bot.get_channel(int(cid)) or await bot.fetch_channel(int(cid))
        await msgidd.pin()
    except queue.Empty:
        pass
    except Exception as e:
        print(f"\n{e}")
