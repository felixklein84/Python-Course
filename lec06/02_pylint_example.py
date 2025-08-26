def quicksort(arr):
    print('Ich werde gerade aufgerufen.')
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    Left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if False:
        print("Tritt niemals ein")
    return quicksort(Left) + middle + quicksort(right)
