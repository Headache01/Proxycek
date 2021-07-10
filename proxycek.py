"""
__author__ = "Headache01"
__date__ = "18/12/2020"
"""
import requests
import json 
import sys

def Proxycek():
    url = 'https://www.proxyscan.io/api/proxy?format=json&type=socks5&limit=1&last_check=300&ping=100'
    r = requests.get(url).json()
    ip = r[0]['Ip']
    port = r[0]['Port']
    ipport = str(ip)+':'+str(port)
    return ipport

def Proxy():

    print('| |  | |              | |          | |         / _ \/_ |')
    print('| |__| | ___  __ _  __| | __ _  ___| |__   ___| | | || |')
    print('|  __  |/ _ \/ _` |/ _` |/ _` |/ __| |_ \ / _ \ | | || |')
    print('| |  | |  __/ (_| | (_| | (_| | (__| | | |  __/ |_| || |')
    print('|_|  |_|\___|\__,_|\__,_|\__,_|\___|_| |_|\___|\___/ |_|')
    print(' ')
    print('\033[1;31;40m'+'Proxy Arama Başlatıldı\n'+'\033[0m')
    a = 0
    while True:
        try:
            sys.stdout.write('\r')
            a += 1
            sys.stdout.write('Denenen Proxy Sayısı: '+str(a))
            sys.stdout.flush()
            testurl = 'https://wtfismyip.com/json'
            ipport = Proxycek()
            httpip = 'socks5://'+ipport
            httpsip = 'socks5://'+ipport
            test = requests.get(testurl,timeout=10,proxies={'http':httpip,'https':httpsip})
            test_icerik = test.json()
            ip = str(test_icerik['YourFuckingIPAddress'])
            konum = test_icerik['YourFuckingLocation']
            tor = str(test_icerik['YourFuckingTorExit'])
            ulke = test_icerik['YourFuckingCountryCode']
            if test.status_code == 200:
                print('\n')
                print('\033[1;32;40m'+'| Proxy Bulundu!'+'\033[0m')
                print('\033[1;33;40m'+'| Kullanılan Proxy: '+ipport+'\033[0m')
                print('\033[1;36;40m'+'| IP: '+ip+'\033[0m')
                print('\033[1;36;40m'+'| Konum: '+konum+'\033[0m')
                print('\033[1;36;40m'+'| Ülke: '+ulke+'\033[0m')
                if tor == False:
                    tor = '\033[1;32;40m'+' Evet'+'\033[0m'
                else:
                    tor = '\033[1;31;40m'+' Hayır'+'\033[0m'
                print('\033[1;36;40m'+'Tor Aktif Mi:'+tor+'\033[0m')
                return ipport
                break
        except:
            pass
