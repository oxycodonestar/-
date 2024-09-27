def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for a in range(m):
            matrix[i].append(value)
        return matrix        
result1 = get_matrix(3,4,6)
result2 = get_matrix(1,2,7)
result3 = get_matrix(22,34,89)
print(result1)
print(result2)
print(result3)