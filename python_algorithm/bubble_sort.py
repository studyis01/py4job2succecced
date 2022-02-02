<<<<<<< HEAD
def bubble_sort(a):
    length = len(a)
    for index in range(length):
        for j in range(1, length - index):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
    return a


=======
def bubble_sort(list):
    length = len(list)
    for index in range(length):
        flag = True
        for j in range(1, length - index):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
                flag = False
        if flag:
            return list
    return list


if __name__ == '__main__':
    list = [1, 10, 3, 8, 5, 4]
    a = bubble_sort(list)
    print(a)
>>>>>>> 1f043fe5e899aafc72e7a7d31f2cd286646a0d72
