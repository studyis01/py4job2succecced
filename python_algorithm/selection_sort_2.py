def selection_sort(list):
    length = len(list)
    for i in range(0, length):
        # 注意你不把 min 分配 if 那里第一次没法做判断
        min = i
        # i + 1 不是 1
        for j in range(i + 1, length):
            if list[min] > list[j]:
                min = j
                list[min], list[i] = list[i], list[min]
            min = i
    return list

if __name__ == '__main__':
    list = [1, 10 , 32, 23, 9 ,6, 8]
    sorted_list = selection_sort(list)
    print(sorted_list)