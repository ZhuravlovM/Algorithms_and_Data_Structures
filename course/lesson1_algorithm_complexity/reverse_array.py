def reverse_array(array):
    reversed_array = []
    for element in range(len(array) - 1, -1, -1):
        reversed_array.append(array[element])
    return reversed_array


original_array = [1, 3, 4, 22, 8, 0]
result = reverse_array(original_array)
print(result)