A = [-3,-2,-1,0,1,4,7]

# Native O(n) searching
if 8 in A:
    print(True)

# Traditional Binary Search - Looking up if number is in Array
# Time: O(logn)
# Space: O(1)

def binary_search(arr, target):

    N = len(arr)
    L = 0
    R = N-1

    while L <= R:
        M = (L + R) // 2

        if arr[M] == target:
            return print(True)
        elif target < arr[M]:
            R = M - 1
        else:
            L = M + 1

    return print(False)

binary_search(A, -2)

# OVERUNDER TECHNIQUE - Based on a Condition
# Time: O(logn)
# Space: O(1)

B = [False,False,False,False,True,True]

def binary_search_condition(arr):

    N = len(arr)
    L = 0
    R = N - 1

    while L < R:
        M = (L + R) // 2

        if B[M]:
            R = M
        else:
            L = M + 1

    return print(L)    

binary_search_condition(B)