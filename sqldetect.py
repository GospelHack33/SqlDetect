import requests
from colorama import Fore
import os
import sys
from cfonts import render
from urllib.parse import urlparse

os.system('clear')
print(render('sqldetect'))

if len(sys.argv) == 3:
    pass
else:
    print('\n[+] Usage - python sqldetect.py -u <url>')
    exit(0)

def validate_url(url):
    o = urlparse(url)
    if o.scheme == 'http' or o.scheme == 'https':
        pass
    else:
        print('\n[+] Invalid Url...\n')
        exit(0)
    if o.query == '':
       print('\n[+] Url Must Contain A Params...\n')
       exit()

validate_url(sys.argv[2])

o = urlparse(sys.argv[2])

# sql inject payload
payload = open('sqlinject.txt', 'r')

num = 0

print(Fore.YELLOW+f'\n[+] Scanning Target - {sys.argv[2]} \n\n[+] Param: {o.query}\n'+Fore.WHITE)

for p in payload:
    send_payload = requests.get(sys.argv[2]+p).text
    if '<b>Notice</b>:' in send_payload or 'A non well formed numeric value encountered in' in send_payload or 'on line {}'.format(num) in send_payload or 'MYSQL Error' in send_payload or 'MySql' in send_payload or '<b>Warning</b>:' in send_payload or 'Warning:' in send_payload:
        num+=1
        print(Fore.GREEN+'\n[+] Sql Injection Is Possible...\n'+Fore.WHITE)
        break
    else:
        print(Fore.RED+'\n[+] Parameter Is Not Injectable...\n'+Fore.WHITE)
        break
