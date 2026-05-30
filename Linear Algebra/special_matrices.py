# Helper: Multiplies two NxN matrices
def multiply_matrix(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

# --- YOUR CODE HERE ---

def get_transpose(matrix):
    n = len(matrix)
    # 1. Create a brand new NxN matrix filled with zeros
    t_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t_matrix[i][j] = matrix[j][i]
    return t_matrix
def is_idempotent(matrix):
    return matrix == (multiply_matrix(matrix, matrix))

def is_orthogonal(matrix):
    identity_matrix = multiply_matrix(get_transpose(matrix), matrix)
    for i in range(len(identity_matrix)):
        for j in range(len(identity_matrix[0])):
            if i == j:
                if identity_matrix[i][j] != 1:
                    return False
            else:
                if identity_matrix[i][j] != 0:
                    return False
    return True

# TEST DATA
idempotent_test = [
    [1, 0],
    [0, 0]
]

# Orthogonal Matrix (90 degree rotation)
orthogonal_test = [
    [0, -1],
    [1,  0]
]

print(f"Test 1 (Should be True): {is_idempotent(idempotent_test)}")
print(f"Test 2 (Should be True): {is_orthogonal(orthogonal_test)}")