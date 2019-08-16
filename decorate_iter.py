"""
装饰器
"""
import time
def decoration_runtime(fun):
    def wrapper(*argsp,**kwargs):
         begin=time.time()
         list_val=fun(*argsp,*kwargs)
         duration=time.time()-begin
         return (list_val,duration)
    return wrapper
"""
建造一个功能型装饰器 ,多装饰器
计算运算时间
"""


@decoration_runtime
def list_sorted(list):
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
    return list


list1=[5,8,9,6,2,3,4,5,5,9,65,8,5,56,3,55,9,8,9,256,26,7]
result=list_sorted(list1)
print(result)

