"""
bubble sort
"""
def bubble_sort(list):
    for j in range(len(list)-1,0,-1):
        for i in range(j):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]


list=[4,54,48,1,2,48,23,48,12,5,49,67,63,24,65]
bubble_sort(list)
print(list)

