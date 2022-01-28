def selection_sort(list):
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
