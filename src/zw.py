import requests,re
print("""\n\tZoomeye discord webhook scraper\n\tBy komodo
\t\t ||\n\t\t ||\n\t\t //\n\t\t// |\\\n\t\t\\\\_//
""");api_key=input("Api Key: ")
rep=set();sus:int=1;D="https://discord.com/api/webhooks"
def check(webhook:str) -> bool:
    return requests.get(webhook).ok
def fix(webhook:str)->str:
    if check(webhook[:-1]):
        return webhook[:-1]
    return webhook
while True:
    print(f"Scraping at page {sus}")
    try:
        params={"query": f'{D}',"page": sus}
        response=requests.get("https://api.zoomeye.org/host/search",headers={"Authorization":f"{api_key}"},params=params)
        pattern=re.compile(r'\b{}\b'.format(D))
        matches=[match.span()[0] for match in pattern.finditer(response.text)]
        for i in matches:
            cook=fix(response.text[i:i+0x79])
            if check(cook) and cook not in rep: 
                print(f"Valid webhook found: {cook}")
                with open("webhookz.txt","a") as thew:thew.write(cook+"\n")
            else:print(f"Invalid or repeated webhook: {cook}")
        if response.text.startswith('{"code": 50005, "error"'):quit("Cannot scrape any other webhooks.")
    except Exception as e: print(f"Error: {e}")
    finally: sus += 1
