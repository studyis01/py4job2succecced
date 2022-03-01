def shell_sort(list):
    length = len(list)
    gap = int(length / 2)
    while gap > 0:
        for i in range(gap, length):
            temp = list[i]
            j = i
            if j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        gap = int(gap / 2)
    return list

if __name__ == '__main__':
    list = [1, 100, 98, 99, 2, 77, 5]
    print(shell_sort(list))


