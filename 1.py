import threading
from time import sleep
import time

def task1(name):
    print("Task 1 %s exexuted."%name)
    sleep(5)

def task2(name):
    print("task2 %s executed. "%name)
    sleep(5)



if __name__:

    print("duoxiancheng:")
    starttime =time.time();
    threads =[]
    t1 = threading.Thread(target=task1,args=("one",))
    threads.append(t1)
    t2 = threading.Thread(target=task2,args=("two",))
    threads.append(t2)



    # t1.start()
    # t1.join()
    # t2.start()
    # t2.join()


    for t in threads:
        t.setDaemon(True) #shouhuxiancheng
        t.start()

    endtime = time.time();
    totaltime = endtime - starttime;
    print("haoshi: {0:.5f}miao".format(totaltime));
    print('-----------')