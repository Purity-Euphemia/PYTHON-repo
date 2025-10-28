num_rows = 3
num_columns = 3


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


for row_index, row in enumerate(matrix):
    row_sum = sum(row)
    print(f"Sum of row {row_index+1}: {row_sum}")


for col_index in range(num_columns):
    column_sum = sum(matrix[row_index][col_index] for row_index in range(num_rows))
    print(f"Sum of column {col_index+1}: {column_sum}")
