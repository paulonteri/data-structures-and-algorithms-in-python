# Binary search function.


def binary_search(list, value):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l+u)//2
        if list[mid] == value:
            return mid
        else:
            if(list[mid] < value):
                l = mid + 1
            else:
                u = mid - 1

    return -1


test_list = [1, 3, 9, 11, 15, 19, 25, 29]


test_val2 = 15
test_val1 = 24

print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
