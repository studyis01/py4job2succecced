def bubble_sort(list):
    length = len(list)
    for index in range(0, length):
        flag = True
        for j in range(1, length - index):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
                flag = False
        if flag:
            return list
    return list

if __name__ == '__main__':
    list = [100, 3, 5, 99, 66]
    print(bubble_sort(list))