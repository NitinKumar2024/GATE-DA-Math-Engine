# --- YOUR CODE HERE ---

def solve_missing_eigenvalues(trace, det, lambda_1):
    # lambda_2 + lambda_3 = trace - lambda_1
    # lambda_2 * lambda_3 = det/lambda_1
    sum_coeff = -(trace - lambda_1)
    product = det/lambda_1
    # x**2 - sum_coeff(x) + product = 0
    # x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
    x1 = (-sum_coeff + ((sum_coeff**2) - 4*1*product)**0.5)/(2*1)
    x2 = (-sum_coeff - ((sum_coeff**2) - 4*1*product)**0.5)/(2*1)
    return (x1, x2)


# TEST DATA from GATE Question
system_trace = 8
system_det = 10
known_lambda = 1

missing_lambdas = solve_missing_eigenvalues(system_trace, system_det, known_lambda)
print(f"The missing eigenvalues are: {missing_lambdas}")