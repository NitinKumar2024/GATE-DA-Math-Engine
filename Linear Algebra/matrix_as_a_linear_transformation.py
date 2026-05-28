# The given 2x2 matrices from the GATE question
A = [[1, 2], 
     [0, 1]]

B = [[1, 1], 
     [1, 1]]

C = [[2, 0], 
     [0, 2]]

# --- YOUR CODE HERE ---
def multiply_2x2(mat1, mat2):
    return [
        [(mat1[0][0] * mat2[0][0]) + (mat1[0][1] * mat2[1][0]), (mat1[0][0] * mat2[0][1]) + (mat1[0][1] * mat2[1][1])],
        [(mat1[1][0] * mat2[0][0]) + (mat1[1][1] * mat2[1][0]), (mat1[1][0] * mat2[0][1]) + (mat1[1][1] * mat2[1][1])]
    ]

def add_2x2(mat1, mat2):
    return [
        [mat1[0][0] + mat2[0][0], mat1[0][1] + mat2[0][1]],
        [mat1[1][0] + mat2[1][0], mat1[1][1] + mat2[1][1]]
    ]

ab = multiply_2x2(A, B)
bc = multiply_2x2(B, C)
top_right_block = add_2x2(ab, bc)

print(top_right_block)