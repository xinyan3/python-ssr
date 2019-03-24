import requests
from ssrdao import *
from bs4 import BeautifulSoup
import base64

'''
test only

'''
data_headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
res1=requests.get('https://github.com/dax309/ssrshare/blob/master/README.md',verify=False,data=data_headers,timeout=10)
soup=BeautifulSoup(res1.text,'html.parser')
dd=soup.find_all('div',class_='highlight highlight-source-shell')
for i in range(len(dd)):
    dd[i]=dd[i].text

str1=''
str1=str1.join(dd)

str1=re.sub("ssr://","\nssr://",str1)
print(str1)
dd=base64.b64encode(bytes(str1,encoding='utf-8'))

with open ('/home/cl/nginx-docker-cl/html/ssr1.txt','a+') as tttt:
    print(str(dd)[2:-1],file=tttt)
            
