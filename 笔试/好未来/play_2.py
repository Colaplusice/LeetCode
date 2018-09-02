x = 3


def many_bin(x):
    bx = bin(x)[2:]
    num = 0
    for each in bx[:-1]:
        if each == '0':
            num += 2
    if bx[-1] == '0':
        num += 2
    else:
        num += 1
    print(num)
    return num
