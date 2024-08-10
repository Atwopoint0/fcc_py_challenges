# Implement selection sort.
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        (array[min_idx], array[i]) = (array[i], array[min_idx])
    return array

print(selection_sort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))