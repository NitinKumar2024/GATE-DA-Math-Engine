def calculate_rank_nullity(matrix_in_row_echelon_form):
    """
    Evaluates a matrix to determine if the original vectors were Independent or Dependent.
    """
    # 1. Count the total number of vectors (rows) you started with
    n_vectors = len(matrix_in_row_echelon_form)
    
    # 2. Assume maximum rank, then subtract 1 for every dead row
    rank = n_vectors
    for row in matrix_in_row_echelon_form:
        if all(element == 0 for element in row):
            rank -= 1

    return rank

# The reduced matrix from your GATE question
test_matrix = [
    [1.0,  2.0, -1.0],
    [0.0,  0.0,  0.0],
    [0.0,  0.0,  0.0]
]
total_columns = 3

rank = calculate_rank_nullity(test_matrix)
nullity = total_columns - rank
print(f"Rank: {rank} | Nullity: {nullity}")
