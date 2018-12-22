import sys

result_list = []


def isTrangle(alist):
    a = [int(s) for s in alist]
    if a[0] + a[1] > a[2] and a[2] - a[0] < a[1]:
        return 1
    elif a[0] == a[1] or a[1] == a[2]:
        return 0
    else:
        return -1


try:
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        sd = list(map(int, (line).split(" ")))
        sd.sort(key=int)
        test1 = sd[:3]
        test2 = sd[1:]
        num1 = isTrangle(test1)
        num2 = isTrangle(test2)

        result = num1 & num2

        if result == 1:
            result_list.append("triangle")
        elif result == 0:
            result_list.append("segment")
        elif result == -1:
            result_list.append("impossible")

except:
    pass
for i in result_list:
    print(i)
