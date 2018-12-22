import random


# list的交换函数
def switch(lists, index_a, index_b):
    temp = lists[index_b]
    lists[index_b] = lists[index_a]
    lists[index_a] = temp


# 随机生成list
def generate_random_list(length=100):
    return [random.randint(0, 100) for i in range(length + 1)]


# 将lists 调小
def mix_list(lists):
    lists = [i for i in lists]

    return []
