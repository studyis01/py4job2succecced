def selection_sort(list):
    length = len(list)
    for i in range(1, length):
        #if list[i] < list[i - 1]:
        min = i
        for j in range(i + 1, length):
            if list[j] < list[min]:
                min = j
                list[min], list[i] = list[i], list[min]
        min = i
    return list