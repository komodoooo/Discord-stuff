from zoomeye.sdk import ZoomEye
import requests as r,re
print("""
\tZoomeye discord webhook scraper\n\tBy komodo
\t\t ||\n\t\t ||\n\t\t //\n\t\t// |\\\n\t\t\\\\_//
""")
zm=ZoomEye(api_key=input("Api Key: "));rep=[]
sus:int=1;d="https://discord.com/api/webhooks"
def check(webhook:str)->bool:
    return r.get(webhook).ok
def fix(webhook:str)->str:
    if check(webhook[:-1]):
        return webhook[:-1]
    return webhook
while True:
    try:
        for i in zm.dork_search(f'{d}',page=sus,resource="host",facets=None):
            b=str(i); s=re.search(d,b).span()[0] if re.search(d,b)!=None else d
            cook=fix(b[s:s+0x79])
            if cook in rep: print(f"Repeated webhook");continue
            elif check(cook):
                print(f"Valid webhook found: {cook}");rep.append(cook)
                with open("webhookz.txt", "a") as thew: thew.write(cook+"\n") 
            else:print("Invalid Webhook")
    except ValueError as e:
        if str(e)=="This page does not exist":quit("Cannot scrape any other webhooks.")
    except TypeError: pass
    finally: sus+=1;print(f"Scraping at page {sus}")
