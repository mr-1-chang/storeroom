"""
队列 queue 先进先出
"""
#创建队列对象
class Queue:
    def __init__(self):
        self.list=[]
    def add(self,value):
        self.list.insert(0,value)
    def pop(self):
        return self.list.pop()
    def show(self):
        for item in range(len(self.list)):
            print(self.list[item],end=" ")

q=Queue()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.add(5)
q.show()
q.pop()
print("=================")
q.show()
