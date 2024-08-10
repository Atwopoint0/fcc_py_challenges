# Given an array of numbers and an argument, find all the element pairs in arr which sum to arg.
# Use the lowest possible indices, where no repeat indices are allowed. Return the sum of the indices.
def pairwise(arr, arg):
    sum = 0
    used_indices = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j] == arg) and (i, j not in used_indices):
                sum += i + j
                used_indices.append(i)
                used_indices.append(j)
    return sum

print(pairwise([1, 4, 2, 3, 0, 5], 7)) # Should return 11.
print(pairwise([1, 3, 2, 4], 4)) # Should return 1.
print(pairwise([1, 1, 1], 2)) # Should return 1.
print(pairwise([0, 0, 0, 0, 1, 1], 1)) # Should return 10.
print(pairwise([], 100)) # Should return 0.