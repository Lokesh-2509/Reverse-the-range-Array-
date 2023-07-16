def reverse_subarray(arr, start_idx, end_idx):
    if start_idx < 0 or end_idx >= len(arr) or start_idx > end_idx:
        return arr
    arr[start_idx:end_idx + 1] = arr[start_idx:end_idx + 1][::-1]
    return arr
A = [1, 2, 3, 4]
B = 2
C = 3
result = reverse_subarray(A, B, C)
print("Reversed array within the range:", result)
A = [2, 5, 6]
B = 0
C = 2
result = reverse_subarray(A, B, C)
print("Reversed array within the range:", result)
