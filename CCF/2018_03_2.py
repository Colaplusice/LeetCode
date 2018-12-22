import sys


def main():
    msg = sys.stdin.readline()
    a_list = msg.strip().split(" ")
    n, L, t = int(a_list[0]), (a_list[1]), int(a_list[2])

    position_list = [[1, int(each)] for each in sys.stdin.readline().strip().split(" ")]
    for i in range(t):
        # print(position_list)
        now_position = [
            [each[0], each[1] + 1] if each[0] == 1 else [each[0], each[1] - 1]
            for each in position_list
        ]
        for each in now_position:
            if each[1] == int(L) or each[1] == 0:

                each[0] *= -1
        # print(now_position)
        for j in range(len(now_position)):
            for k in range(j + 1, len(now_position)):
                if now_position[k][1] == now_position[j][1]:
                    now_position[k][0] *= -1
                    now_position[j][0] *= -1
        position_list = now_position
    print(" ".join(str(each) for each in map(lambda x: x[1], position_list)))


main()
