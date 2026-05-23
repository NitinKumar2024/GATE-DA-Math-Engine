def check_data_redundancy(matrix_in_row_echelon_form):
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

    print(f"Total Vectors: {n_vectors} | Mathematical Rank: {rank}")

    # 3. The Core Logic
    if rank == n_vectors:
        return "Result: Linearly INDEPENDENT (Pure Data - Basis Candidate)"
    else:
        return "Result: Linearly DEPENDENT (Redundant Data - Contains Junk)"

# Testing the exact vectors from your GATE Crucible (after Gaussian Elimination)
final_matrix = [
    [1.0,  2.0, -1.0],
    [0.0, -3.0,  6.0],
    [0.0,  0.0,  0.0]  # The dead row you found mathematically
]

print(check_data_redundancy(final_matrix))