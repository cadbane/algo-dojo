def find_min_index(arr):
    min_value = arr[0]
    min_index = 0

    for idx, value in enumerate(arr):
        if value < min_value:
            min_value = value
            min_index = idx

    return min_index


def selection_sort(arr):
    result = []

    for j in range(len(arr)):
        smallest = find_min_index(arr)
        result.append(arr.pop(smallest))

    return result


if __name__ == '__main__':
    little_list = [6,7,8,3,9,3,0,4,1]
    print('before:', little_list)
    print('after:', selection_sort(little_list))

    from random import randint
    big_list = [randint(n, n*n) for n in range(1000)]
    print('before:', big_list)
    print('after:', selection_sort(big_list))