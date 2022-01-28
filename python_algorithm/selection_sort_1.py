def selection_sort(list):
    length = len(list)
    for i in range(0, length):
        min = i
        for j in range(i + 1, length):
            if list[min] > list[j]:
                min = j
                list[min], list[i] = list[i], list[min]
            min = i
    return list


if __name__ == '__main__':
    a = [1, 9, 7, 3]
    sorted = selection_sort(a)
    print(sorted)
