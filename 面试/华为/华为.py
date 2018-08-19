# encoding=GBK
# str='wqes大addwewe....'
str=input()
# print(str)
length=input()
length=int(length)
index=0
ass=['b','a','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
     'A','B','C','D','E','F','G','H','I','J','K','L''M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
     ]
sout=''
for each in str:
    if index<length:
        if each.isspace():
            continue
        if each in ass:
            index+=1
            sout+=each
        elif each.isdigit():
            index+=1

        elif each.isalnum():
            index+=1
            sout+=each

        else:
            index+=2
            if index<length:
                sout+=each
    else:
        break
print(sout)