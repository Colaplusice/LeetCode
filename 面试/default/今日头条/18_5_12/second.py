#coding=utf-8



if __name__ == '__main__':

    sd=input()
    a=sd.split(" ")
    m= int (a[0])
    n=int(a[1])
    dic={}
    result=[]
    for i in range(m):
        line=input()
        alpha=line[0]
        if not dic.has_key(alpha):
            dic[alpha]=[line]
        else:
            dic[alpha].append(line)
    for t in range(n+1):
        is_find=False
        lines=input()
        if lines=='':
            continue
        alphas=lines[0]
        if not dic.has_key(alphas):
            result.append(-1)
            continue
        else:
            for each in dic[alphas]:
                if each in lines:
                    result.append(1)
                    is_find=True
                    break
        if is_find==False:
            result.append(-1)

    for each in result:
        print(each)
