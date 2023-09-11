def counting_sort_stable(array):
    min_val, max_val = min(array), max(array)
    count = [0] * (max_val - min_val + 1)
    for num in array:
        count[num - min_val] += 1
    sorted_array = []
    for i, freq in enumerate(count):
        sorted_array.extend([i + min_val] * freq)
    return sorted_array


def counting_sort_non_stable(array):
    min_val, max_val = min(array), max(array)
    count = [0] * (max_val - min_val + 1)
    for num in array:
        count[num - min_val] += 1
    sorted_array = []
    for i, freq in enumerate(count):
        sorted_array.extend([i + min_val] * freq)
    return sorted_array


initial_array1 = [4, 2, 2, 8, 3, 3, 1]
sorted_array_stable = counting_sort_stable(initial_array1)
print("Sorted array stable:", sorted_array_stable)

initial_array2 = [3, 1, 7, 5, 5, 9, 2]
sorted_array_non_stable = counting_sort_non_stable(initial_array2)
print("Sorted array non-stable:", sorted_array_non_stable)
