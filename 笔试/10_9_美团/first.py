def question_a():
    """
    测试用例
5 20
7 8 5 3 7


    :return:
    """
    a = input().split(" ")
    X = int(a[1])
    price_list = input().split(" ")
    price_list = [int(each) for each in price_list]
    price_list.sort(reverse=True)
    add_list = []
    print(price_list)
    all = 0
    for each in price_list:
        if all >= X:
            add_list.sort()
            for each in add_list:
                if all - each >= X:
                    all -= each
                else:
                    continue
            return all
        if all + each > X:
            price_list.reverse()
            for each in price_list:
                if all > X:
                    break
                all += each
                add_list.append(each)
        all += each
        add_list.append(each)


if __name__ == "__main__":
    result = question_a()

    print(result)
