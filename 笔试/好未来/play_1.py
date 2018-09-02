a = input()
max_num = 0
stack = []
for each in reversed(a):
    if int(each) % 3 == 0:
        max_num += 1
    else:
        stack.insert(0, each)
        for i_2 in range(len(stack)):
            if stack[:i_2] and int(''.join(stack[:i_2])) % 3 == 0:
                stack = []
                max_num += 1
                break
print(max_num)