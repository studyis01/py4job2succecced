def selection_sort(list):
    length = len(list)
    # 0
    for i in range(0, length):
        min = i
        for j in range(i + 1, length):
            if list[j] <= list[min]:
                min = j
                #
                list[min], list[i] = list[i], list[min]
            min = i
    return list