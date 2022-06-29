import requests
import threading
import itertools

owo = open(input("Webhooks file: "), "r").read().splitlines()

def main(webhook, content):
    proxyuwu={
        "http": next(itertools.cycle(["https://95.0.206.53:8080", "https://133.242.237.138:3128", 
                                    "https://20.81.62.32:3128", "https://150.136.139.34:3128"]))
    }       #https://free-proxy-list.net/
    r=requests.post(webhook, data={"content":content}, proxies=proxyuwu)
    if not str(r.status_code).startswith(str(0x02)):
        print("oh no", r.status_code)
    else: print("uwu~")
try:
    c = str(input("content: "))
    while True: 
        for lel in owo:
            threading.Thread(target=main(lel, c), args=()).start()
except Exception as neg: print(neg)
