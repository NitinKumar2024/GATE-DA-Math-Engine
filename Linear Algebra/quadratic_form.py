# The 3x3 Hessian Matrix
H = [
    [ 2, -1,  0],
    [-1,  2, -1],
    [ 0, -1,  2]
]

# --- YOUR CODE HERE ---

def classify_loss_landscape(matrix):
    # 1. Calculate D1
    # 2. Calculate D2
    # 3. Calculate D3
    # 4. Return classification string
    D1 = matrix[0][0]
    D2 = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    D3 = (matrix[0][0] * ((matrix[1][1] * matrix[2][2]) - (matrix[2][1] * matrix[1][2])))  + (-matrix[0][1] * ((matrix[1][0] * matrix[2][2]) - (matrix[2][0] * matrix[1][2]))) + (matrix[0][2] * ((matrix[1][0] * matrix[2][1]) - (matrix[2][0] * matrix[1][1])))

    if D1 > 0 and D2 > 0 and D3 > 0:
        return "Positive Definite"
    elif D1 < 0 and D2 > 0 and D3 < 0:
        return "Negative Definite"
    elif D2 < 0:
        return "Indefinite (Saddle Point)"
    elif D1 == 0 or D2 == 0 or D3 == 0:
        return "Semi-Definite"
    else:
        return "Something Wrong in Calculation"
landscape_shape = classify_loss_landscape(H)
print(f"The Optimizer detects: {landscape_shape}")