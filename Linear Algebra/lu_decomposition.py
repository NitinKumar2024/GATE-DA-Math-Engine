# The Matrix from the GATE Question
A = [
    [2, -1,  1],
    [4,  1, -1],
    [2,  2,  1]
]

# --- YOUR CODE HERE ---
def get_first_column_multipliers(matrix):
    pivot = matrix[0][0]
    if pivot == 0:
        return "Error: Zero Pivot requires Row Swapping"
    L21 = matrix[1][0] / pivot
    L31 = matrix[2][0] / pivot
    return f"L21: {L21}, L31: {L31}"

print(get_first_column_multipliers(A))