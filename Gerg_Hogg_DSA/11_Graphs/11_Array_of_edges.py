# Array of Edges (Directed) [Start, End]

n = 8
A = [[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,2],[4,5],[5,2]]

print("----------ARRAY OF EDGES----------\n",A)

# Convert Array of Edges -> Adjacency Matrix

M = []
for i in range(n):
    M.append([0] * n)

for u, v in A:
    M[u][v] = 1

print("\n----------ADJACENCY MATRIX----------\n",M)

# TO Make the graph in Dictionary
# Convert Array of Edges -> Adjacency List

from collections import defaultdict

D = defaultdict(list)

for u, v in A:
    D[u].append(v)

print("\n----------ADJACENCY LIST----------\n",D)

# TO Check how a Edge is connected to 

# MATRIX
print("MATRIX OF A SPECIFIC EDGE:-",M[2])

# LIST
print("LIST OF A SPECIFIC EDGE:-",D[3])