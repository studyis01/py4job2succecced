def bubble_sort(list):
    length = len(list)
    for i in range(length):
        flag = True
        for j in range(1, length - i):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
                flag = False
        # 层级错了
        if flag:
            return list
    return list

if __name__ == '__main__':
    list = [1, 100, 98, 99, 2, 77, 5]
    print(bubble_sort(list))