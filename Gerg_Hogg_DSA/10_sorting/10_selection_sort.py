# Selection Sort
# Time: O(n^2)
# Space: O(1)

A = [-3,3,2,1,-5,6,2,-3]

def selection_sort(arr):
    n = len(arr)
    for i in range (n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

selection_sort(A)
print(A)
