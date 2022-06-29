import aiohttp
import asyncio
import random

async def main():
    print("""
HAKAI MASS REPORTER
"Don't get cocky. HAKAI!" -Lord beerus, god of destruction"
Sex Features: more faster with asyncio and aiohttp requests

Author: Komodo\n 
""")

    async with aiohttp.ClientSession() as sexion:
        tokens = open(input("Tokens file: "), "r").read().splitlines()
        try:
            gi = int(input('Guild id:'))
            ci = int(input('Channel id:'))
            mi = int(input('Message id:'))  
        except ValueError:
            print("Type a numeric value, NIGGER!")
        agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
        for token in tokens:
            headerss = {
                "User-Agent": agent,    #https://user-agents.net/random
                "Authorization": token,
                "Content-type": "application/json"
            }
            jsonn = {
                'channel_id': ci,
                'guild_id': gi,
                'message_id': mi,
                'reason': random.randint(1,5)
            }
            print("Reason: random.\nRange:6969\nHAKAI!")
            try:
                for sex in range(6969):
                    async with sexion.post("https://discord.com/api/v9/report", headers=headerss, json=jsonn) as beerus:
                        if beerus.status == 201:
                            print(f"Done. {sex}")
                        else:
                            print(f"Something Wrong. {beerus.status}")
            finally:
                print("Hakai finished.")
                exit()     
                
asyncio.run(main())
