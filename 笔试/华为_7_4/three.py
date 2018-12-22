a = input()
num = int(a)

num_list = list(a)

num_list = [int(s) for s in num_list]

result_list = [0] * 100
result_list[-1] = num
mutl_list = list(range(num)[1:])
for i in mutl_list:
    print(i)
    for index, each in enumerate(reversed(result_list)):
        print((index, each))
        up = 0
        result_list[index] *= i
        if result_list[index] >= 10:
            print("here")
            print((index, each))
            up += result_list[index] // 10
            result_list[index] %= 10
        # 有进位
        if up:
            print((index, each))
            print(up)
            result_list[index - 1] += up
            print(result_list)
print(result_list)
