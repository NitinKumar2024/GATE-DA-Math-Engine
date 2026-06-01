# The GATE Question Vectors
target_a = [1, 1]
data_b = [2, 4]

# --- YOUR CODE HERE ---

def dot_product(v1, v2):
    value = 0
    for i in range(len(v1)):
        value += (v1[i] * v2[i])
    return value

def scalar_multiply(scalar, v):
    n_vector = [scalar * v[i] for i in range(len(v))]
    return n_vector


def vector_subtract(v1, v2):
    n_vector = [v1[i] - v2[i] for i in range(len(v1))]
    return n_vector

def calculate_projection(a, b):
    # 1. Calculate the scalar multiplier: (a^T b) / (a^T a)
    # 2. Calculate projection vector p
    # 3. Calculate error vector e
    # 4. Return p, e
    scalar = (dot_product(a, b) / dot_product(a, a))
    p = scalar_multiply(scalar, a)
    e = vector_subtract(b, p)
    return (p, e)

p, e = calculate_projection(target_a, data_b)
print(f"Projection (p): {p}")
print(f"Error (e): {e}")