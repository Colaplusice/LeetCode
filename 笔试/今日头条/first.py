# encoding=utf-8
# 输入： 第1行为n代表用户的个数 第2行为n个整数，第i个代表用户标号为i的用户对某类文章的喜好度
# 第3行为一个正整数q代表查询的组数  第4行到第（3+q）行，每行包含3个整数l,r,k代表一组查询，
# 即标号为l<=i<=r的用户中对这类文章喜好值为k的用户的个数。
# # 数据范围n <= 300000,q<=300000 k是整型
# 5
# 1 2 4 4 5
# 3
# 1 2 1
# 2 4 5
# 3 5 3
# 1
# 0
# 2
# import time
num_user = input()
like = raw_input()
Num_like = like.split(" ")
like_dict = {}
for index, i in enumerate(Num_like):
    if not like_dict.has_key(i):
        like_dict[i] = [index]
    else:
        like_dict[i].append(index)
groups = input()
message_list = []
# input
for i in range(groups):
    rowMessage = raw_input()
    message_list.append(rowMessage.split(" "))
# deal
# start=time.time()

for each in message_list:
    try:

        begin = int(each[0]) - 1
        end = int(each[1])
        point = each[2]
        result = 0
        # print('begin:{} end:{}'.format(begin,end))
        for i in range(begin, end):
            if i in like_dict[point]:
                result += 1
        print(result)
    except KeyError:
        print(0)
    # print(len(filter(lambda x:x==each[2],Num_like[int(each[0])-1:int(each[1])])))
# end=time.time()
# print(end-start)
