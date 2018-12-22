def transfer(num):
    alist = []
    while num != 0:
        if num % 2 == 0:
            alist.append(0)
        else:
            alist.append(1)
        num = num // 2
    print(alist)


transfer(200)
