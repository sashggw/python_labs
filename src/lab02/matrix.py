#////////////////////////////TRANSPOSE///////////////////////////////////////
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    for i in range(len(mat)):
        if len(mat[i]) != len(mat[0]):
            return 'TypeError:матрица рваная '
            
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]


print("transpose")
print(f"[[1, 2, 3]]→{transpose([[1, 2, 3]])}")
print(f"[[1], [2], [3]]→{transpose([[1], [2], [3]])}")
print(f"[[1, 2], [3, 4]]→{transpose([[1, 2], [3, 4]])}")
print(f"[]→{transpose([])}")
print(f"[[1, 2], [3]]→{transpose([[1, 2], [3]])}")

#////////////////////////////ROWS_SUMS///////////////////////////////////////
def row_sums(mat: list[list[float | int]]) -> list[float]:
    for i in range(len(mat)):
            if len(mat[i]) != len(mat[0]):
                return 'TypeError:матрица рваная '


    return [sum(row) for row in mat]

print("row_sums")
print(f"[[1, 2, 3], [4, 5, 6]]→{row_sums([[1, 2, 3], [4, 5, 6]])}")
print(f"[[-1, 1], [10, -10]]→{row_sums([[-1, 1], [10, -10]])}")
print(f"[[0, 0], [0, 0]]→{row_sums([[0, 0], [0, 0]])}")
print(f"[[1, 2], [3]]→{row_sums([[1, 2], [3]])}")

#////////////////////////////COL_SUMS///////////////////////////////////////

def col_sums(mat: list[list[float | int]]) -> list[float]:
    for i in range(len(mat)):
                if len(mat[i]) != len(mat[0]):
                    return 'TypeError:матрица рваная '


    return [sum(col) for col in zip(*mat)]
#либо можно было сделать transpose ,а потом row_sums :p
print("col_sums")
print(f"[[1, 2, 3], [4, 5, 6]]→{col_sums([[1, 2, 3], [4, 5, 6]])}")
print(f"[[-1, 1], [10, -10]]→{col_sums([[-1, 1], [10, -10]])}")
print(f"[[0, 0], [0, 0]]→{col_sums([[0, 0], [0, 0]])}")
print(f"[[1, 2], [3]]→{col_sums([[1, 2], [3]])}")