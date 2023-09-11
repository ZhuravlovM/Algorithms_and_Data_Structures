def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


initial_array = [21, 9, 14, 55, 80, 33, 76]
insertion_sort(initial_array)
print("Sorted array:", initial_array)
