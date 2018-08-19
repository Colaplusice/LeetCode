
a = [12322, 23, 324, 12, 9, 8, 23, 5443, 0, 1, 1, 4,10000]


def part(array,left,right):
    '''
     以最右边元素作为基准元素 小于基准元素的放在左边,position计算小于元素的个数
     最后position位置上的元素是大于基准元素的第一个元素
     最后拿最右边的元素和position 交换，完成分区
     返回值为position,
    :param array:
    :param left:
    :param right:
    :return: position
    '''
    # switch(index, right, array)
    position = left
    for i in range(left,right):
        if array[i] < array[right]:
            array[position],array[i]=array[i],array[position]
            position += 1
    array[position],[right]=array[right],[position]
    return position


def sort(left, right, array):
    if left >= right:
        return
    '''
    找一个基准元素进行分区
    然后递归执行
    '''
    position = part(array,left,right)
    sort(left, position - 1, array)
    sort(position + 1, right, array)


if __name__ == '__main__':
    # position = part(a)
    # print(position)

    # print(a)
    sort(0, len(a)-1,a)

    print(a)
