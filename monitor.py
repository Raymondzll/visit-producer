import requests
import bs4
import sys
import os
po=os.popen('tasklist |find /c /i "pythonw.exe"')
value=int(po.readlines()[0][:-1])
if value>0:
        print(value,'pythonw program(s) running!')
        exit()
#site='https://note.ms/225192'
#if len(sys.argv)>1:
#        site=sys.argv[1]
#r=requests.get(site)
#r.raise_for_status()
#soup=bs4.BeautifulSoup(r.text,"html.parser")
#e=soup.select('body div.stack div.layer div.layer div.layer textarea.content')
#print(e[0].string)
