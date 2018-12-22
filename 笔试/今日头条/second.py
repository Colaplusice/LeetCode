# encoding=utf-8
# 作为一个手串艺人，有金主向你订购了一条包含n个杂色串珠的手串——每个串珠要么无色，要么涂了若干种颜色。
# 为了使手串的色彩看起来不那么单调，金主要求，手串上的任意一种颜色（不包含无色），
# 在任意连续的m个串珠里至多出现一次（注意这里手串是一个环形）。手串上的颜色一共有c种。
# 现在按顺时针序告诉你n个串珠的手串上，每个串珠用所包含的颜色分别有哪些。
# 请你判断该手串上有多少种颜色不符合要求。即询问有多少种颜色在任意连续m个串珠中出现了至少两次。

first_row = raw_input()

first_list = first_row.split(" ")

n = int(first_list[0])
m = int(first_list[1])
c = int(first_list[2])

zhu = [[] for iss in range(n)]

error = 0
for i in range(n):
    input_row = raw_input()
    sd = input_row.split(" ")
    for each in sd[1:]:
        zhu[i].append(each)
    # for i_2 in zhu[i:i+m%len(zhu)]:
    #     if(sd==sv for sd in i_2 for sv in each):
    #         error+=1


print(zhu)


for index, each in enumerate(zhu):
    for i_2 in zhu[index : index + m % len(zhu)]:
        if (sd == sv for sd in i_2 for sv in each):

            error += 1
