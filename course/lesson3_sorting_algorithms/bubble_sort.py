def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


initial_array = [21, 9, 14, 55, 80, 33, 76]
bubble_sort(initial_array)
print("Sorted array:", initial_array)
