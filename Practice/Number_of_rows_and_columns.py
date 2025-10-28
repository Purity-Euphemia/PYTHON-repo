
num_rows = 3
num_columns = 3

matrix = []


for row_index in range(num_rows):
    current_row = []
    for col_index in range(num_columns):
        value = int(input(f"Enter value for row {row_index+1}, column {col_index+1}: "))
        current_row.append(value)
    matrix.append(current_row)


print("\nYour 2D matrix is:")
for row in matrix:
    print(row)


second_row_third_col = matrix[1][2]
print(f"\nElement at 2nd row, 3rd column: {second_row_third_col}")
