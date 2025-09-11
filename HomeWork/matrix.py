matrix = [[0 for _ in range(10)] for _ in range(10)]

for count in range(10):
    for counter in range(10):
        matrix[count][counter] = count * counter
        for row in matrix:
            print(row)

