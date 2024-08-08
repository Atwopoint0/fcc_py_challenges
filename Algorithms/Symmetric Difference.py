# Define a function that takes the symmetric difference of multiple sets without using the '^' method on sets.
# Note the formula 'A XOR B = (A - B) OR (B - A)'.
# We could also use this formula element-wise or directly use symmetric difference instead.
def sym(*args):

    base = set()
    for i in range(len(args)):
        a_minus_b = set(args[i]) - base
        b_minus_a = base - set(args[i])
        base = a_minus_b | b_minus_a
    return base

print(sym([1, 2, 3], [5, 2, 1, 4])) # Should return [3, 4, 5].
print(sym([1, 2, 3], [5, 2, 1, 4])) # Should contain only three elements.
print(sym([1, 2, 3, 3], [5, 2, 1, 4])) # Should return [3, 4, 5].
print(sym([1, 2, 3, 3], [5, 2, 1, 4])) # Should contain only three elements.
print(sym([1, 2, 3], [5, 2, 1, 4, 5])) # Should return [3, 4, 5].
print(sym([1, 2, 3], [5, 2, 1, 4, 5])) # Should contain only three elements.
print(sym([1, 2, 5], [2, 3, 5], [3, 4, 5])) # Should return [1, 4, 5].
print(sym([1, 2, 5], [2, 3, 5], [3, 4, 5])) # Should contain only three elements.
print(sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5])) # Should return [1, 4, 5].
print(sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5])) # Should contain only three elements.
print(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3])) # Should return [2, 3, 4, 6, 7].
print(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3])) # Should contain only five elements.
print(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])) # Should return [1, 2, 4, 5, 6, 7, 8, 9].
print(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])) # Should contain only eight elements.