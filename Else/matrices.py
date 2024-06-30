def create_mat(i,j):
    mat = []
    for column in range(i):
        mat.append([])
        for row in range(j):
            mat[-1].append(0)
    return mat

print(create_mat(5,6))