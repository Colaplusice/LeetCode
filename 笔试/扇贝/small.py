str_result = "1\n2  4\n3  6  9\n4  8 12 16\n5 10 15 20 25\n6 12 18 24 30 36\n7 14 21 28 35 42 49\n8 16 24 32 40 48 56 64\n9 18 27 36 45 54 63 72 81\n"
test_list = [1, 2, 3, 2, 1, 10, 5, 5, 1]


def double_nine():
    strs = ""
    for i_1 in range(1, 10):
        for i_2 in range(1, i_1 + 1):

            results = i_1 * i_2
            if results < 10 and i_2 > 1:
                if i_2 != i_1:
                    strs += " " + str(results) + " ".join()
                else:
                    strs += " " + str(results)
            else:
                if i_2 != i_1:
                    strs += str(results) + " "
                else:
                    strs += str(results)

        strs += "\n"
    return strs


def duplicated_list(lists):
    result_list = []
    dicts = {}
    for i in lists:
        if not dicts.get(i):
            dicts[i] = 1
        else:
            dicts[i] += 1

    for i in lists:
        if dicts[i] > 1:
            result_list.append(i)
        else:
            pass
    return result_list

    pass


if __name__ == "__main__":
    # double_nine()
    duplicated_list(test_list)
