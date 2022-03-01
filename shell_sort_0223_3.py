def shell_sort(list):
    length = len(list)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            temp = list[i]
            j = i
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        gap = gap // 2
    return list