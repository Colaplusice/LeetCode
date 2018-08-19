a=input()
result=0
if a<=10:
    result=3.5
else:
    result=3.5+int(a-10)*0.75

print("%.2f"%result)