# Build Min Heap (Heapify)
# Time: O(n) Space: O(1)

A = [-4,3,1,0,2,5,10,8,12,9]

import heapq
heapq.heapify(A)

print("----------MIN HEAP (HEAPIFY)----------\n" + f"{A}")

# Heap Push (Insert Element)
# Time: O(log n)

heapq.heappush(A, 4)

print("\n----------HEAP PUSH----------\n" + f"{A}")

# Heap Pop (Extract Min)
# Time: O(log n)

min = heapq.heappop(A)

print("\n----------HEAP POP----------\n" + f"{A}")

# Heap Sort
# Time: O(n log n) Space: O(n)
# IMP: O(1) Space is possible via swapping, but it is complex

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
        min = heapq.heappop(arr)  
        new_list[i] = min


    return print(new_list)  

# Heap Push Pop 
# Time: O(log n)

heapq.heappushpop(A , 23)
print("\n----------HEAP PUSH POP----------\n" + f"{A}")


# Heap max

B = A
n = len(B)

for i in range(n):
    B[i] = -B[i]

heapq.heapify(B)
print("\n----------HEAP MAX----------\n" + f"{B}")


# Build HEAP from Scratch Time: O(n log n)

C = [-2,-1,0,22,33,4,9]

heap = []
print("\n----------HEAP FORMING----------\n")
for x in C:
    heapq.heappush(heap, x)
    print(heap)

print("\n----------FINAL OUTPUT----------\n" + f"{heap}")