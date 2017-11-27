def binary_search(list, item):
    low, high = 0, len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)

        if list[mid] == item:
            return mid

        if list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return None


if __name__ == '__main__':

    a = [1,2,3,4,5,6,7,8,9,10]
    print(binary_search(a, 4))

    b = [n*n for n in range(100000)]
    print(binary_search(b, 77))
    print(binary_search(b, 970225))