def shell_sort(list):
    length = len(list)
    gap = int(length / 2)
    #
    while gap > 0:
        for i in range(gap, length):
            temp = list[i]
            j = i
            # while gap >= 0 and list[length - gap] > temp:
            while j >= gap and list[j - gap] > temp:
                # list[j] = list[gap - i]
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        gap = int(gap / 2)
    return list

if __name__ == '__main__':
    list = [1, 100, 98, 99, 2, 77, 5]
    print(shell_sort(list))
