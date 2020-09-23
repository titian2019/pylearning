'''md5碰撞脚本 需要字典'''
import hashlib
src='6846860684f05029abccc09a53cd66f1'
def get_line():
    f = open('1.txt') #默认mode=‘r’
    print( 'start:')
    while True:
        line = f.readline()
        if len(line)==0:
            print ('line 0')
            break
        m1 = hashlib.md5()
        m1.update(line.encode('utf-8'))
        tmp =m1.hexdigest()
        print (line[:-1]+"  :"+tmp)
        if tmp==src:
            print (src+': md5对应的值为：'+line)
            break

get_line()