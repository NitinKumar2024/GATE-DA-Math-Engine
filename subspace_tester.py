def verify_subspace(condition_rule, valid_vector_1, valid_vector_2, test_scalar):
    """
    Tests a mathematical condition against the Three Golden Rules of Subspaces.
    """
    print(f"--- Running Subspace Diagnostics ---")

    # RULE 1: The Zero Vector Test
    zero_vector = (0.0, 0.0, 0.0)
    if not condition_rule(zero_vector):
        return " FAILED: Zero Vector (0,0,0) is not allowed. NOT a subspace."
    print("PASSED: Zero Vector Test")

    # RULE 2: Scalar Multiplication Test
    # Multiply valid_vector_1 by the test_scalar
    scaled_v = (
        valid_vector_1[0] * test_scalar, 
        valid_vector_1[1] * test_scalar, 
        valid_vector_1[2] * test_scalar
    )
    if not condition_rule(scaled_v):
        return f" FAILED: Scalar Multiplication. Vector {scaled_v} broke the rule. NOT a subspace."
    print("PASSED: Scalar Multiplication Test")

    # RULE 3: Addition Test
    # Add valid_vector_1 and valid_vector_2 together
    added_v = (
        valid_vector_1[0] + valid_vector_2[0],
        valid_vector_1[1] + valid_vector_2[1],
        valid_vector_1[2] + valid_vector_2[2]
    )
    if not condition_rule(added_v):
        return f" FAILED: Vector Addition. Vector {added_v} broke the rule. NOT a subspace."
    print(" PASSED: Vector Addition Test")

    return " ALL TESTS PASSED: This acts like a valid Subspace!"

# Define the GATE condition from Option A
def rule_A(vector):
    x, y, z = vector
    # Returns True if the equation equals 0, False otherwise
    return (x + 2*y - 3*z) == 0
def rule_B(vector):
    x, y, z = vector
    # TASK 1: Return True if x multiplied by y equals 0, else False
    return (x*y) == 0

# TASK 2: Define two valid 3D vectors based on your paper calculation
v1 = 5, 0, 0 
v2 = 0, 6, 0 
scalar = 2.0


# Run the engine
result = verify_subspace(rule_B, v1, v2, scalar)
print(result)