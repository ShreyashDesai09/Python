# Merg Sort
# Time: O(n log n)
# Space: O(n)

A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return print(arr)
    
    m = len(arr) // 2
    L = arr[:m]
    R = arr[m:]

    L = merge_sort(L)
    R = merge_sort(R)
    l, r = 0, 0 


    