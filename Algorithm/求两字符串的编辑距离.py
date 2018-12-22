def min_distance(self, str_a, str_b):
    len_a = len(str_a)
    len_b = len(str_b)
    if len_a != len_b:
        return False
    dis = [[0 for i in range(len_a + 1)] for j in range(len_b + 1)]
    for i in range(len_a + 1):
        dis[0][i] = i
    for j in range(len_b + 1):
        dis[j][0] = j

    for i in range(1, len_b + 1):
        for j in range(1, len_a + 1):
            new_value = (
                dis[i - 1][j - 1]
                if str_a[j - 1] == str_b[i - 1]
                else dis[i - 1][j - 1] + 1
            )
            dis[i][j] = min(dis[i - 1][j] + 1, dis[i][j - 1] + 1, new_value)
    if dis[len_b][len_a] == 1:
        print(dis)
        return True
    print(dis)
    return False
