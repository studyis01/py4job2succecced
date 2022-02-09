def bubble_sort(list):
    length = len(list)
    for i in range(length):
        flag = True
        # 1, length - i
        for j in range(1, length - i):
            # i - 1, i
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
                flag = False
        if flag:
                # 没有发生交换，直接返回list
            return list
    return list