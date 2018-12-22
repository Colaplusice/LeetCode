def kmp(str_s, sub_str_s):
    if not sub_str_s:
        return True
    if not str_s:
        return False

    partial_list = []

    for each in str_s:
        pass

    sub_len = len(sub_str_s)
    begin_length = len(str_s) - len(sub_str_s)

    return False


def calculate_partial(strs):
    partial_list = [0] * len(strs)
    for index, each in enumerate(strs):
        print(each)
        value = 0
        for i in range(index):
            if strs[i] == strs[index - i]:
                value += 1
            else:
                break
        partial_list[index] = value

    return partial_list


if __name__ == "__main__":
    res = kmp("hello", "ll")
    res = calculate_partial("abcdabd")
    print(res)
