import requests, re
a = requests.get("https://discord.com/api/v10/users/@me", headers={"Authorization":input("\n token: ")}).json()
rgx = re.split("{|'|}", str(a).replace(",", "\n"))
print("\n "+"".join([i for i in rgx]), "\n")
