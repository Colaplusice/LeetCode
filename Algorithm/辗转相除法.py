def Mindivisor(a,b):
    print('sd')
    if a%b:
        Mindivisor(b,a%b)
    return b


result=Mindivisor(30,12)
print(result)

