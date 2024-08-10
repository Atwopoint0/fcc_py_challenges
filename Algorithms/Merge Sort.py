# Implement merge sort.
def merge(left, right):
    result = []
    i = 0 
    j = 0
    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
 
def merge_sort(array):
    if len(array) <= 1:
        return array
 
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
 
    return merge(left, right)

print(merge_sort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))