# Matrix A from the GATE question
A = [
    [2,  5, -1],
    [0,  3,  4],
    [0,  0, -1]
]
det_B = 4
scalar = 2
dimension = 3

# --- YOUR CODE HERE ---
def get_triangular_det(matrix):
    det_matrix = 1
    for i in range(len(matrix)):
        det_matrix *= matrix[i][i]
    return det_matrix

def apply_scalar_trap(original_determinant, scalar, dimension):
    return ((scalar**dimension) * original_determinant)

# 1. Get |A|
det_A = get_triangular_det(A)

# 2. Get |A^T| (It's the same as |A|)
det_A_transpose = det_A

# 3. Get |A^T B|
det_AB = det_A_transpose * det_B

# 4. Apply the scalar trap to get |2(A^T B)|
final_answer = apply_scalar_trap(det_AB, scalar, dimension)

print(f"Final Determinant |C|: {final_answer}")