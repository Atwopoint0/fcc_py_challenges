# Implement insertion sort.
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        insert_idx = i
        insert_val = array[i]
        for j in range(i - 1, -1, -1):
            if array[j] > insert_val:
                array[j + 1] = array[j]
                insert_idx = j
            else:
                break
        array[insert_idx] = insert_val
    return array
print(insertion_sort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))