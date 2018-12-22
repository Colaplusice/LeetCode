# 0 1 1 1 1 1 1 1 1 0

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result_list = []

ind = input()
index_list = ind.split(" ")

temp_list = []
max_type = 1
for index, num in enumerate(a):
    if index_list[index] == 0:
        max_type *= 2
        temp_list.append([0, num * 2])
    temp_list.append([num])


for i in range(max_type):

    pass
