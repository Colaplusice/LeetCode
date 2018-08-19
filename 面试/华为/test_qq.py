# a=input()
# print(a)
# list_a=list(a)
# sd=list(set(list_a))
# sd.sort(key=list_a.index)
# sd.reverse()
# str=''
# for each in sd:
#     str+=each
# print(int(str))

tmp=input()

s=float(tmp)

a=[(-150,-1000),(0,700),(40,940),(300,3000),(650,7500)]

def cal(input_x):
    min=10000
    which=0
    if input_x < float(-150):
        return -1000
    if input_x>650:
        return 7500
    for index,each in enumerate(a):
        if abs(input_x-each[0])<min:
            min=abs(input_x-each[0])
            which=index

    if which==0:
        result=formulate(a[0],a[1],input_x)
    else:
        if a[which][0]-a[which-1][0]<=a[which+1][0]-a[which][0]:
            result=formulate(a[which-1],a[which],input_x)
        else:
            result=formulate(a[which],a[which+1],input_x)
    return result

def formulate(x0,x1,x):
    result=x0[1]+((x-x0[0])*x1[1]-(x-x0[0])*x0[1])/(x1[0]-x0[0])
    return result
result=cal(s)


print(result)