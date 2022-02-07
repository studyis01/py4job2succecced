def insert_sort(list):
    length = len(list)
    for i in range(1, length):
        if list[i - 1] > list[i]:
            index = i
            temp = list[i]
            for j in range(i - 1, -1, -1):
                # > 要比的数要小，才能排在前面，升序
                if list[j] > temp:
                    list[j + 1] = list[j]
                    index = j
                else:
                    break
            list[index] = temp
    return list

if __name__ == '__main__':
    list = [1, 10, 99, 87, 65, 4, 100]
    print(insert_sort(list))