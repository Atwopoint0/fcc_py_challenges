# Implement quick sort. (Hoare parition scheme).

def partition(array, lo, hi):
    pivot = array[lo]
    i = lo - 1
    j = hi + 1

    while True:
        i += 1
        j -= 1
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i>= j:
            return j
        (array[i], array[j]) = (array[j], array[i])

def quick_sort(array, lo = 0, hi = None):
    if hi is None:
        hi  = len(array) - 1
    if lo >= 0 and hi >= 0 and lo < hi:
        p = partition(array, lo, hi)
        quick_sort(array, lo, p)
        quick_sort(array, p + 1, hi)
    return array

print(quick_sort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))
