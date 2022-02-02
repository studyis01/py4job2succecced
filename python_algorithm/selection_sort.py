def selection_sort(list):
<<<<<<< HEAD
    length = len(list)
    for i in range(0, length):
        min = i
        for j in range(i + 1, length):
            if list[j] <= list[min]:
                min = j
                list[min], list[i] = list[i], list[min]
            min = i
    return list

if __name__ == '__main__':
    list = [1, 10 , 32, 23, 9 ,6, 8]
    sorted_list = selection_sort(list)
    print(sorted_list)
=======
    n = len(list)
    for i in range(0, n):
        min = i
        for j in range(i + 1, n):
            if list[j] < list[min]:
                min = j
                a[min], a[i] = a[i], a[min]
            min = i
    return list


if __name__ == '__main__':
    a = [1, 9, 7, 3]
    sorted = selection_sort(a)
    print(sorted)
>>>>>>> 1f043fe5e899aafc72e7a7d31f2cd286646a0d72
