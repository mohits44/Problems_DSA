arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
left = 0
right = len(arr) - 1

while left < right:
    while arr[left] == 0 and left < right:
        left += 1
    while arr[right] == 1 and left < right:
        right -= 1

    if left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp

print(arr)
