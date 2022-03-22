# def bubble_sort(list):
#     flag = True
#     length = len(list)
#     for i in range(0, length):
#         for j in range(1, length - i):
#             if flag == False:
#                 return list
#             else:
#                 if list[j] < list[j - 1]:
#                     list[j], list[j - 1] = list[j - 1], list[j]
#     return list
def bubble_sort(list):
    length = len(list)
    for i in range(0, length):
        flag = True
        for j in range(1, length - i):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
                flag = False
        if flag:
            return list
    return list

if __name__ == '__main__':
    list=[1,5,4,3,7,9]
    print(bubble_sort(list))