"""
iteration.py
"""


# list=[1,2,3,4,5,6,7,8,9]
# list_iterator=list.__iter__()
# while True:
#     try:
#         data=list_iterator.__next__()
#         print(data)
#     except StopIteration or Exception as e:
#         print(e)
#         break
"""
迭代器 参与到 for循环
"""
class Range:
    def __init__(self, bigen,end, step):
        self.bigen=bigen
        self.end=end
        self.step=step
    def __iter__(self):
        return Iteration(self.end,self.bigen,self.step)
class Iteration:

    def __init__(self, end=None, bigin=None, step=None):
        self.end=end
        self.bigen=bigin
        self.step=step
        self.ele=self.bigen-self.step


    def __next__(self):
        if self.ele <self.end-self.step:
            self.ele +=self.step
        else:
            raise  StopIteration
        return self.ele

for item in Range(1,5,2):
    print(item)