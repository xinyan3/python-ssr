#!/usr/bin/python
# -*- coding: <UTF-8> -*-

import requests
import base64
import os,time,datetime
import sys
from Crypto.Cipher import AES
import json,ast
import re
import redis
from ssrdao import *
#r.set('name', 'zhangsan')
#print((r['name']))
def dao():
    ss=os.getcwd()
    print(ss)
    sys.path.append(ss)
    

    with open ('/home/cl/nginx-docker-cl/html/url.txt','r') as f:
        lines = f.readlines()
        miwen=lines
    f.close()
    data_headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
    res1=requests.get('https://raw.githubusercontent.com/AmazingDM/sub/master/ssrshare.com',verify=False,data=data_headers,timeout=100)
    dd=res1.text
    print(dd)

    miwen=str(miwen[0])
    miwen=dd+miwen
    print(miwen)
    print(type(miwen))
    decrypted_text =str(base64.b64decode(miwen),encoding='utf-8')

    decrypted_text=decrypted_text

    mimi='MTg1LjEzMy4xOTMuMjA1Ojg4NjY6b3JpZ2luOnJjNDpwbGFpbjpiRzVqYmk1dmNtYy8/b2Jmc3BhcmFtPSZyZW1hcmtzPTVyU2I1cDJKNTUtMlFRJmdyb3VwPWJHNWpiaTV2Y21j'
    print(decrypted_text)
    rtt=decrypted_text.splitlines()
    print(len(rtt))

    for i in range(len(rtt)):
    #tttt =base64.b64decode(decrypted_text)
    #print(tttt)
        rtt[i]=re.sub("ssr://","",rtt[i])
        rtt[i]=re.sub("–","+",rtt[i])
        rtt[i]=re.sub("_","/",rtt[i])
    # rtt[i]=zhenze(rtt[i])

    # rtt[i]=str(base64.b64decode(rtt[i]))
        #print(rtt[i][2:-1])
    
        rtt[i]=parse_ssr(rtt[i])
        with open ('/home/cl/nginx-docker-cl/html/ssr.txt','a+') as tttt:
            print(str(rtt[i]),file=tttt)
            print(rtt[i])
        tttt.close()

dao()

