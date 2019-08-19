"""
消息队列演示
注意： 消息存入与去除关系为 先入先出
"""
from multiprocessing import Process,Queue
from random import randint
from time import  sleep
#建立消息队列
q=Queue(5)

def request():
    for i in range(10):
        x=randint(1,100)
        y=randint(1,100)
        data=(x,y)
        q.put(data)
def hanld():
    if not q.empty():
        for  i in range(10):
            data=q.get()
            print("x+y=",data[0]+data[1])
            sleep(2)


p=Process(target=request)
p1=Process(target=hanld)
p.start()
p1.start()

p.join()
p1.join()




