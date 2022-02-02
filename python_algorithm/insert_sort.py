def insert_sort(list):
    length = len(list)
    for i in range(1, length):
        if list[i] < list[i - 1]:
            temp = list[i]
            index = i
            for j in range(i - 1,-1,-1):
                if list[j] > temp:
                    list[j + 1] = list[j]
                    index = j
                else:
                    break
            list[index] = temp
    return list