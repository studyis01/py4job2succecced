def insert_sort(list):
    length = len(list)
    for i in range(1, length):
        if list[i] < list[i - 1]:
            temp = list[i]
            index = i
            # 记得要缩进
            for j in range(i - 1, -1, -1):
                # 是 大于 不是 小于，和取出元素大的元素交换
                if list[j] > temp:
                    list[j + 1] = list[j]
                    # 下标保存是 index，不是temp
                    index = j
                else:
                    break
            # list[index]不是list[j]
            list[index] = temp
    return list

if __name__ == '__main__':
    list = [1, 10, 99, 87, 65, 4, 100]
    print(insert_sort(list))