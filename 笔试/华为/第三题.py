# 有N个骰子，同时投掷出去，向上面的数字之和为 A。
# 那么输入为N个筛子，请计算出A，和他出现的概率。
# 概率值，小数点保留5位。

# 1
# [[1, 0.16667], [2, 0.16667], [3, 0.16667], [4, 0.16667], [5, 0.16667], [6, 0.16667]]
bit = input("Enter a binary digit:")
if bit == 0 or bit == 1:
    print("your input is", bit)
else:
    print(bit)
    print(type(bit))
    print(type(1))
    print("your input is invalid")
