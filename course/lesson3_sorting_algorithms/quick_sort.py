def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_lomuto(array):
    if len(array) <= 1:
        return array

    pivot = array[-1]
    left = []
    right = []
    equal = []

    for num in array:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)

    return quick_sort_lomuto(left) + equal + quick_sort_lomuto(right)


def quick_sort_hoare(array, low, high):
    if low < high:
        pivot_index = partition_hoare(array, low, high)
        quick_sort_hoare(array, low, pivot_index)
        quick_sort_hoare(array, pivot_index + 1, high)


def partition_hoare(array, low, high):
    pivot = array[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while array[i] < pivot:
            i += 1

        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]


initial_array1 = [23, 11, 34, 87, 6, 18, 52]
sorted_array1 = quick_sort(initial_array1)
print("Quick Sort:", initial_array1)

initial_array2 = [64, 34, 25, 12, 22, 11, 90]
sorted_array2 = quick_sort(initial_array2)
print("Quick Sort Lomuto:", initial_array2)

initial_array3 = [12, 31, 19, 94, 28, 1, 74]
quick_sort_hoare(initial_array3, 0, len(initial_array3) - 1)
print("Quick Sort Hoare:", initial_array3)
