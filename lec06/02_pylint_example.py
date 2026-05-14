def quicksort(arr):
    print('I am being called right now.')
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    Left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if False:
        print("This branch is never reached")
    return quicksort(Left) + middle + quicksort(right)
