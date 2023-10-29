s = int(input())
mat = [[i for i in range(1, s + 1)] for j in range(s)]
for row in mat:
    print(", ".join(map(str, row)))
for i in range(s):
    for j in range(i + 1, s):
        mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
print("\n")
for row in mat:
    print(", ".join(map(str, row)))
