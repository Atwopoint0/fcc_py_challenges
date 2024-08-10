# Implement bubble sort with optional optimisations.
# Optimisation 1: The n-th pass finds the n-th largest element.
# Optimisation 2: All elements after the last swap are already sorted.
def bubble_sort(array):
    n = len(array)
    new_n = n
    while new_n > 0:
        new_n = 0
        for i in range(1, n):
            if array[i-1] > array[i]:
                (array[i-1], array[i]) = (array[i], array[i-1])
                new_n = i
        n = new_n
    return array
print(bubble_sort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))
