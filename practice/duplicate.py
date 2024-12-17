arr = [1, 2, 3, 4, 5, 3, 2, 6]

for i in range(len(arr)):
    if arr[i] not in arr[i + 1:]:
        print(arr[i])
