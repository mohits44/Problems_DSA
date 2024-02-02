def sort012(arr, n):
    low = 0
    mid = 0
    high = n - 1
    for i in range(0, n):
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high = high - 1

# Example usage:
arr = [1, 0, 2, 1, 0, 2]
n = len(arr)
sort012(arr, n)
print(arr)
