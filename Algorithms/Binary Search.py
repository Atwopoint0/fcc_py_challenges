def binary_search(array, value):        
    path = []
    lo = 0
    hi = len(array) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if array[mid] < value:
            lo = mid + 1
            path.append(array[mid])
        elif array[mid] > value:
            hi = mid - 1
            path.append(array[mid])
        else:
            path.append(array[mid])
            return path
    return "Value Not Found"

testArray = [
  0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
  23, 49, 70
]
print(binary_search(testArray, 0)) # Should return [13, 5, 2, 0].
print(binary_search(testArray, 1)) # Should return [13, 5, 2, 0, 1].
print(binary_search(testArray, 2)) # Should return [13, 5, 2].
print(binary_search(testArray, 6)) # Should return the string 'Value Not Found'.
print(binary_search(testArray, 11)) # Should return [13, 5, 10, 11].
print(binary_search(testArray, 13)) # Should return [13].
print(binary_search(testArray, 70)) # Should return [13, 19, 22, 49, 70].