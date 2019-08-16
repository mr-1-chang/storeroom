"""
iteration.py
"""
list=[1,2,3,4,5,6,7,8,9]
list_iterator=list.__iter__()
while True:
    try:
        data=list_iterator.__next__()
        print(data)
    except StopIteration or Exception as e:
        print(e)
        break