def merge_sort(list):
    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]
    return merge(left, right)

def merge(left, right):
    result = []
    l, r = 0, 0
    if len(list) <= 1:
        return list
    #
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(l)