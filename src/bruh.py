import requests, threading

owo=open(input("Webhooks file: "), "r").read().splitlines()
body=requests.get("https://sslproxies.org").text
proxies:list=body[body.find("UTC.\n")+6:44116].splitlines()
proxies.remove(proxies[-1])
COUNT:int=0

class Task(threading.Thread):
    def run(f, a:tuple):
        threading.Thread(target=f, args=a, daemon=True).start()

def main(webhook, content):
    global COUNT
    proxyuwu={"https":"http://%s"%proxies[COUNT]}
    try:
        r = requests.post(webhook,data={"content":content},proxies=proxyuwu)
        if r.ok:
            print(f'"{content}" successfully sent.')
        elif r.status_code==429:
            if COUNT>=len(proxies)-1: COUNT=0
            else: COUNT+=1
    except: pass

try:
    c = str(input("content: "))
    while True:
        for lel in owo:
            Task.run(main,(lel,c))
except Exception as neg: exit("SUS")
