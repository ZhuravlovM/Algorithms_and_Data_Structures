def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


sorted_array = [2, 5, 9, 10, 18, 24, 27, 31, 35, 39, 45]
desired_number = 24
result = binary_search(sorted_array, desired_number)

if result != -1:
    print(f"Number {desired_number} is found and has index: {result}.")
else:
    print(f"Number {desired_number} is not found in array.")