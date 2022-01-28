def bubble_sort(a):
    length = len(a)
    for index in range(length):
        for j in range(1, length - index):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
    return a


