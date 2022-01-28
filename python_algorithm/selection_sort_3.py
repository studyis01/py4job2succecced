def selection_sort(list):
    length = len(list)
    for i in range(0,length):
        min = i
        for j in range(i + 1, length):
            if list[j] < list[min]:
                min = j
                #list[j + 1] = list[j]
                # i bushi j
                list[i], list[min] = list[min], list[i]
            min = i
    return list