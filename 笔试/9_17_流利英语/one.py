# @Time    : 2018/9/17 下午8:23


def find_big_list(value_list):
    max_value = 0
    return_value = value_list[0]
    for value in value_list:
        if max_value < 0:
            max_value = 0
        max_value += value
        if max_value > return_value:
            return_value = max_value
    print(return_value)


if __name__ == "__main__":

    length = int(input())
    i = 0
    value_list = []
    while i < length:
        value = input()
        value_list.append(int(value))
        i += 1
    find_big_list(value_list)
