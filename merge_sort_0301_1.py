def merge_sort(list):
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
        # 层级错误
    if len(left) == l:
        # left right 不分
        for i in right[r:]:
            result.append(i)
    else:
        for i in left[l:]:
            result.append(i)
    return result

if __name__ == '__main__':
    list = [9, 3, 89, 100, 72, 33, 66]
    sorted = merge_sort(list)
    print(sorted)
    # print(cProfile.run(merge_sort(list)))