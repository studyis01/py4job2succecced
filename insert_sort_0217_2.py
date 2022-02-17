def insert_sort(list):
    length = len(list)
    for i in range(1, length):
        if list[i] < list[i - 1]:
            index = i
            temp = list[i]
            for j in range(i - 1, -1, -1):
                if list[j] > temp:
                    list[j + 1] = list[j]
                    index = j
                else:
                    break
            list[index] = temp
    return list

if __name__ == '__main__':
    list = [1, 100, 98, 99, 2, 77, 5]
    print(insert_sort(list))
