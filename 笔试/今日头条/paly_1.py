a=[]
b=[]
with open('text','r') as opener:
    line=opener.readline()
    while line:
        a.append(line)
        line=opener.readline()

with open('text_2','r') as opener:
    line=opener.readline()
    while line:
        b.append(line)
        line=opener.readline()
i=0
for i_1,i_2 in zip(a,b):
    i+=1
    if i_1!=i_2:
        print(i_1)
        print(i)
        print(i_2)
