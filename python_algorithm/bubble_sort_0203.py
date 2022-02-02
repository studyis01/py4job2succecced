def bubble_sort_flag(list):
    length = len(list)
    # range 不是 list
    for index in range(0, length):
        flag = True
        for j in range(1, length - index):
            # 注意下标的变化
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
                flag = False
        #
        if flag:
            return list
    return list

if __name__ == '__main__':
    list = [1, 10, 3, 8, 5, 4]
    a = bubble_sort_flag(list)
    print(a)