def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat: return []

    width = len(mat[0])
    for row in mat:
        if len(row) != width: raise ValueError("Рваная матрица")

    return [[mat[i][j] for i in range(len(mat))] for j in range(width)]
# print(transpose([[1, 2, 3]]))    
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]])) 
# print(transpose([]))     
# print(transpose([[1, 2], [3]]))                


def row_sums(mat: list[list[float | int]]) -> list[float]:
    for i in range(len(mat)):
            if len(mat[i]) != len(mat[0]): raise ValueError('Матрица рваная ')

    return [sum(row) for row in mat]
# print(row_sums([[1, 2, 3], [4, 5, 6]]))   
# print(row_sums([[-1, 1], [10, -10]]))    
# print(row_sums([[0, 0], [0, 0]]))     
# print(row_sums([[1, 2], [3]]))      


def col_sums(mat: list[list[float | int]]) -> list[float]:
    for i in range(len(mat)):
                if len(mat[i]) != len(mat[0]): raise ValueError('Матрица рваная ')
                    
    return [sum(col) for col in zip(*mat)]
print(row_sums([[1, 2, 3], [4, 5, 6]]))   
print(row_sums([[-1, 1], [10, -10]]))    
print(row_sums([[0, 0], [0, 0]]))     
print(row_sums([[1, 2], [3]]))     
