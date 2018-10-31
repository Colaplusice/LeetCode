def base_kmp(str_s, sub_str_s):
    if not sub_str_s:
        return True
    if not str_s:
        return False
    sub_len = len(sub_str_s)
    begin_length = len(str_s) - len(sub_str_s)
    for i in range(begin_length):
        if str_s[i:sub_len + i] == sub_str_s:
            return True

    return False


if __name__ == '__main__':
    res = base_kmp('hello', 'll')
    print(res)
