matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = []

for col_index in range(len(matrix[0])):
    transposed_row = []
    for row_index in range(len(matrix)):
        transposed_row.append(matrix[row_index][col_index])
    transposed_matrix.append(transposed_row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)
