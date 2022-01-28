def bubble_sort(list):
    length = len(list)
    for index in range(length):
        flag = True
        for j in range(1, length - index):
            # 写成小于号了
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
                flag = False
        # 放错地方了
        if flag:
            return list
    return list