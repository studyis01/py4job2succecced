def selection_sort(list):

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




