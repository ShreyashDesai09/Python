def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new matrix with dimensions cols x rows
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    
    return result

# Example usage
matrix = [
    [10, 20],
    [30, 40],
    [50, 60]
]

transposed = transpose(matrix)
for row in transposed:
    print(row)
