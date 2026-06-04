# The 3x2 Matrix from the GATE Question
A = [
    [ 1,  1],
    [ 0,  1],
    [-1,  1]
]

# --- PREVIOUS ENGINE HELPERS ---
def get_transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def multiply_matrix(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# --- YOUR CODE HERE ---

def get_singular_values(matrix):
    # 1. Get A_T
    # 2. Get ATA = A_T * A
    # 3. Find Trace and Det of the 2x2 ATA matrix
    # 4. Find lambdas using the quadratic formula: (-b +- sqrt(b^2 - 4ac)) / 2a
    #    (Remember: a = 1, b = -Trace, c = Det)
    # 5. Return the square roots of the lambdas
    A  = matrix
    A_T = get_transpose(A)
    ATA = multiply_matrix(A_T, A)
    trace_value = ATA[0][0] + ATA[1][1]
    determinant = (ATA[0][0] * ATA[1][1]) - (ATA[0][1] * ATA[1][0])
    sum_coeff = -trace_value
    product = determinant
        # x**2 - sum_coeff(x) + product = 0
    # x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
    x1 = (-sum_coeff + ((sum_coeff**2) - 4*1*product)**0.5)/(2*1)
    x2 = (-sum_coeff - ((sum_coeff**2) - 4*1*product)**0.5)/(2*1)
    return (x1**0.5, x2**0.5)

sigmas = get_singular_values(A)
print(f"Singular Values (sigma_1, sigma_2): {sigmas}")