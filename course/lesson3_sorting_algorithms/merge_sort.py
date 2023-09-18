def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left_half = array[:middle]
    right_half = array[middle:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


initial_array = [16, 18, 9, 2, 12, 6]
sorted_array = merge_sort(initial_array)
print("Sorted array:", sorted_array)