size = int(input())
matrix = [[i for i in range(1, size + 1)] for j in range(size)]
for row in matrix:
    print(", ".join(map(str, row)))
for i in range(size):
    for j in range(i + 1, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print("\n")
for row in matrix:
    print(", ".join(map(str, row)))

