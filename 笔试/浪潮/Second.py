import sys


def isTrangle(alist):
    ad = [int(s) for s in alist]
    if ad[0] + ad[1] > ad[2] and ad[2] - ad[0] < ad[1]:
        return 1
    elif ad[0] == ad[1] or ad[1] == ad[2]:
        return 0
    else:
        return -1


alist = []
if __name__ == "__main__":
    a = raw_input()
    while a:
        try:
            sd = a.split(" ")
            sd.sort(key=int)
            test1 = sd[:3]
            test2 = sd[1:]
            num1 = isTrangle(test1)
            num2 = isTrangle(test2)

            result = num1 & num2

            if result == 1:
                alist.append("triangle")
                sys.stdout.writelines("triangle" + "\n")
            elif result == 0:
                alist.append("segment")

                sys.stdout.writelines("segment" + "\n")
            elif result == -1:
                alist.append("impossible")

                sys.stdout.writelines("impossible" + "\n")
            a = raw_input()
        except:
            pass
