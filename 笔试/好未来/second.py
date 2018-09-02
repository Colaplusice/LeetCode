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
    return num


rows = int(input())
value = 0

for i in range(rows):
    row = input()
    x = int(row.split(' ')[0])
    k = int(row.split(' ')[1])
    bin_x = bin(x)[2:]
    have_nums = many_bin(x)
    if k < have_nums:
        if k % 2 == 0:
            y = '1' + k // 2 * '0'
            print(int(y, 2))
        else:
            y='1'+(k//2-1)*'0'+'1'
            print(int(y,2))
            continue
        value = '1'
    rest_nums = k - have_nums
    if rest_nums % 2 == 0:
        y ='1'+(rest_nums // 2 - 1) * '0' + bin_x
        value = int(y, 2)
    else:
        y = '1' + (rest_nums // 2 - 1) * '1' + bin_x
        value = int(y, 2)
    print(value)
