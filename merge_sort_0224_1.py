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

    if l == len(left):
        for i in right[r:]:
            result.append(i)
    else:
        for i in left[l:]:
            result.append(i)

    return result

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)

if __name__ == '__main__':
    a = [14, 2, 34, 43, 21, 19]
    print (merge_sort(a))