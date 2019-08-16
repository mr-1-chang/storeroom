"""
queue_link.py
"""
class Node:
    def __init__(self, value,next=None):
        self.value=value
        self.next=next
class Lkqueue:
    def __init__(self):
        self.head=self.tail=Node(None)
    def add(self,value):
        #建立一个中间变量,隔离
        self.tail.next=Node(value)
        if not self.head.value:
            self.head=self.tail.next
        self.tail=self.tail.next
    def pop(self):
        val=self.head.value
        self.head=self.head.next
        return val
l1=Lkqueue()
l1.add(8)
l1.add(7)
l1.add(6)
l1.add(5)
l1.add(4)
print(l1.pop())
print(l1.pop())
print(l1.pop())



