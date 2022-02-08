def insert_sort(list):
    length = len(list)
    for i in range(1, length):
        if list[i] < list[i - 1]:
            index = i
            temp = list[i]
            for j in range(i -1, -1, -1):
                # if temp > list[j]:
                #     temp = list[j]
                #     list[j + 1] = list[j]
                if temp < list[j]:
                    index = j
                    list[j + 1] = list[j]
                else:
                    break
            list[index] = temp
    return list