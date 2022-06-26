from colorama import *
import requests
import json
import os

def waff_kontrol(site):
    liste = json.loads(open("waff.json","r").read())
    try:
        req = requests.get(site,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36"},timeout=15)
    except:
        print(f" {Fore.YELLOW}[!] {Fore.WHITE}Siteye istek gönderilemiyor, lütfen daha sonra tekrar deneyin.")
        exit()
    for i in liste:
        if (liste[i] in req.headers['Server']):
            return i
    return ""

def banner():
    if (os.name=="nt"):
        os.system("cls")
    else:
        os.system("clear")
    print(f"""{Fore.GREEN}
   __    __ _           _   __    __       __  __ 
  / / /\ \ \ |__   __ _| |_/ / /\ \ \__ _ / _|/ _|
  \ \/  \/ / '_ \ / _` | __\ \/  \/ / _` | |_| |_ 
   \  /\  /| | | | (_| | |_ \  /\  / (_| |  _|  _|
    \/  \/ |_| |_|\__,_|\__| \/  \/ \__,_|_| |_|  

  ---> {Fore.WHITE}Bu yazılım Umut Şahin tarafından kodlanmıştır.
                                                
    """)

def main():
    banner()
    print(f" {Fore.MAGENTA}[?] {Fore.WHITE}Güvenlik duvarını kontrol etmek istediğiniz siteyi giriniz: ",end="")
    site = input()
    waff = waff_kontrol(site)
    if (waff == ""):
        print(f" {Fore.RED}[!] {Fore.WHITE}Sitede herhangi bir güvenlik duvarı bulunamadı.")
    else:
        print(f" {Fore.GREEN}[+] {Fore.WHITE}Sitede bulunan güvenlik duvarı: {waff}\n")

if (__name__=="__main__"):
    try:
        init()
        main()
    except KeyboardInterrupt:
        exit()
