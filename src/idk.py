import requests,re
t:str=input("\n token: ")
if len(t)==30:t=f"Bearer {t}"
a=requests.get("https://discord.com/api/v10/users/@me",headers={"Authorization":t}).json()
rgx=re.split("{|'|}",str(a).replace(",","\n"))
print("\n "+"".join([i for i in rgx]),"\n")
