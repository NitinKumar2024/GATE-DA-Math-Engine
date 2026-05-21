# The Engineering Challenge
# Imagine your Gaussian Elimination loop has just finished running. You have a variable n which is the number of variables (e.g., n = 3), and you have your final matrix.

# To find the rank in Python, you simply need to count how many rows survived.

# Your task:
# Write a simple conceptual logic or Python pseudo-code to check the final state of the matrix.

# How would you tell the computer to find rank_A (counting rows that have non-zero numbers in the variable columns)?

# How would you tell the computer to find rank_AB (counting rows that have non-zero numbers across the entire row)?

# How would you write the if/elif/else block using rank_A, rank_AB, and n to print either "Unique Solution", "No Solution", or "Infinitely Many Solutions"?

def check_system_consistency(matrix, n_variables):
    """
    Evaluates a matrix in Row Echelon Form to determine the system's consistency.
    """
    n_rows = len(matrix)
    
    # Assume maximum rank initially, we will subtract if we find dead rows
    rank_a = n_rows
    rank_ab = n_rows
    
    for row in matrix:
        # Check the left side (Coefficient Matrix A)
        # row[:-1] slices the list to exclude the very last element (the constant)
        if all(element == 0 for element in row[:-1]):
            rank_a -= 1
            
            # If the left side is dead, check the right side (the constant)
            # row[-1] gets the very last element
            if row[-1] == 0:
                rank_ab -= 1 

    # The Decision Logic (Exactly as you wrote it!)
    if rank_a != rank_ab:
        return "No Solution (Inconsistent)"
    elif rank_a == rank_ab == n_variables:
        return "Unique Solution"
    elif rank_a == rank_ab < n_variables:
        return "Infinitely Many Solutions"
    else:
        return "System error."

# Your test matrix
matrix = [
    [1, 2, 3, 4],
    [0, 2, 6, 8],
    [0, 0, 0, 5]
]

result = check_system_consistency(matrix, n_variables=3)
print(result)