# 自动售货机里有 N 瓶复制可乐。复制可乐非常神奇，喝了它的人会复制出一个自己来！
# 现在有 Alice, Bob, Cathy, Dave 四个人在排队买复制可乐。买完的人会马上喝掉，然后他和他的副本会重新去队伍的最后面排队买可乐。
# 问最后一个买到复制可乐的人叫什么名字？
alice = 1
##  i+4*(i-1)
# alice+=4*i+i
##
##


def main():
    N = input()
    name_list = ["Alice", "Bob", "Cathy", "Dave"]

    N = int(N)
    i = 1
    alice = 1
    while N > alice:
        alice += 4 * i + i
        # print(alice)
        i += 1
    print(alice)
    alice -= 4 * (i - 1) + i - 1
    print(alice)


# 1, 5,6  13 14 15 16
main()
