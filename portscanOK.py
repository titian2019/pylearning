'''端口扫描'''
import socket
import threading
import time
import datetime
alll=0
duankou=''
def changshi(ip,port):    #端口扫描函数
    socket.setdefaulttimeout(2)
    so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip=ip
    po=port
    global alll
    global duankou
    try:
        soo=so.connect((ip,po))
        print(po,'ok')
        alll+=1
        duankou+=str(po)
        duankou+=','
    except Exception as err:
        #print(po,str(err))
        pass

ip=input('ip:')
stt=datetime.datetime.now()
st=time.time()
print(stt)
port1=0
port2=65535
def shuru(): #检查输入的端口是否合法
    try:
        port1=int(input('范围：'))
        port2=int(input('{}--'.format(port1)))
        return port1,port2
    except ValueError as err:
        print(err)
        shuru()
shuru()
if port2>port1:pass
else:port1,port2=port2,port1

print(port1,'--',port2)
threads=[]
a=input('go?:')
for i in range(port1,port2):
    t=threading.Thread(target=changshi,args=(ip,i))
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()
et=time.time()

print('all:',alll)
print('time:',(et-st),'s')

sa=input('save?y/n:')
if sa=='y':
    with open('scanjieguoOK.txt', 'a') as f:  #保存扫描到的端口
        f.write('all:')
        f.write(str(alll))
        f.write(' ')
        f.write(duankou)
        f.write('\n')
