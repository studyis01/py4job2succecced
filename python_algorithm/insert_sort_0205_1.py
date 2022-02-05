def insert_sort(list):
    length = len(list)
    for i in range(1, length):
        if list[i] < list[i - 1]:
            index = i
            temp = list[i]
        for j in range(i - 1, -1, -1):
            if list[j] < temp:
                list[j + 1] = list[j]
                temp = j
            else:
                break
        temp = list[j]
    return list
