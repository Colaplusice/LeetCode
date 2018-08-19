

def Search(array,find_num):
    if len(array)==1:
        return 1
    low=0
    high=len(array)
    while low<=high:
        middle= int ((low+high)/2)
        if array[middle]>find_num:
            high=middle-1
        elif array[middle]<find_num:
            low=middle+1
        else:
            return middle
a=[1,2,3,4,5,6,7,9]
s=Search(a,6)
print(s)