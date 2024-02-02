def square_matrix_map(matrix=None):
    if matrix is None:
        matrix = []
    return list(map(lambda row: list(map(lambda col: col**2, row)), matrix))
