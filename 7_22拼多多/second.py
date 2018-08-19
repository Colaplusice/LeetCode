# 四年一度的世界杯又来了！小多在公司内发起了一个票选最强球星的活动。共有 N 个候选球星，
# 每位投票者需要在选票上为每位候选球星评定一个实例等级，
# 等级由英文字母表示，'a' 级最高，'z' 级最低，共26级。
# 我们称候选球星 X 强于候选球星 Y，当「 X 的评级比 Y 高」的票数高于「 Y 的评级比 X 高」的票数。
# 若一个候选球星强于任一其他候选球星时，则称该球星为“球王”。根据这个规则，至多只会有一个球王。
# 需要注意的是也可能没有球王。
# 现在给出所有 M 张选票，请你帮小多判断一下哪位候选球星是球王。
# ab cd 为等级 index 为球员     每个index 建一个dict 记录 其他球员比他高的数量
# 遍历 acbd
# 4 3
# acbd
# bacd
# bdca

def char_toInt(strs):
    return [ord(i) for i in strs]
def which_pass(a_list,b_list):
    v_1=0
    v_2=0
    # print('alist{} and blist{}'.format(a_list,b_list))
    for i_1, i_2, in zip(a_list,b_list):
        # print(i_1,i_2)
        if i_1<i_2:
            v_1+=1
        elif i_1>i_2:
            v_2+=1
    if v_1>v_2:
        return b_list
    elif v_2>v_1:
        return a_list
    else:
        return None



import sys
def main():
    # 读取第一行的n
    input_list = sys.stdin.readline().strip().split(' ')
    # print(input_list)
    star = int(input_list[0])
    vote = int(input_list[1])
    vector = []
    # ans = 0
    for i in range(vote):
        #     读取每一行
        line = sys.stdin.readline().strip()
        if line:
            vector.append(char_toInt(line))

    dict_list = []
    dicts = {}
    # print(vector)
    for i in vector:
        for index, each in enumerate(i):
            if dicts.get(index):
                dicts[index].append(each)
            else:
                dicts[index] = [each]
    pass_dict = {}
    for i in range(star):
        for j in range(i + 1, star):
            # print('this is i {}j{}'.format(i,j))
            # 没有被pass
            if pass_dict.get(i) and pass_dict.get(j):
                continue
            i_list = dicts.get(i)
            j_list = dicts.get(j)
            pass_list = which_pass(i_list, j_list)
            if pass_list == i_list:
                # print('-'*20)
                # print('pasjslist is i_list')
                # print(i_list,j_list)
                pass_dict[i] = 'pass'
            elif pass_list == j_list:
                # print('-' * 20)
                # print('passlist is j_list')
                # print(i_list, j_list)
                pass_dict[j] = 'pass'
            else:
                pass_dict[i] = 'pass'
                pass_dict[j] = 'pass'
    # print(pass_dict)
    for i in range(star):
        if not pass_dict.get(i):
            print(i)
            return
    print(-1)


    # print(dicts)


if __name__ == "__main__":
    main()