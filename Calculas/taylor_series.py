import math

class CalculusEngineV2:
    def maclaurin_exp(self, x, terms):
        """
        Approximates e^x using the Maclaurin series.
        'terms' is the number of items in the polynomial (e.g., terms=3 means 1 + x + x^2/2!)
        """
        approximation = 0
        # YOUR CODE HERE
        for i in range(0, terms):
            approximation += ((x**i)/math.factorial(i))

        return approximation

    def maclaurin_sin(self, x, terms):
        """
        Approximates sin(x) using the Maclaurin series.
        Hint: The powers for sine are always ODD (1, 3, 5, 7...). 
        The signs alternate (+, -, +, -).
        """
        approximation = 0
        for n in range(terms):
            power = 2 * n + 1               # Generates 1, 3, 5, 7...
            sign = (-1)**n                  # Generates +1, -1, +1, -1...
            approximation += sign * (x**power) / math.factorial(power)
            
        # YOUR CODE HERE
        return approximation

# --- THE CRUCIBLE TESTING SUITE ---
if __name__ == "__main__":
    engine = CalculusEngineV2()
    
    # Let's test x = 2.0
    test_val = 2.0
    
    print("--- e^x Approximation ---")
    print(f"True value (math.exp): {math.exp(test_val)}")
    for n in [2, 5, 10]:
        print(f"Maclaurin (n={n}): {engine.maclaurin_exp(test_val, n)}")
        
    print("\n--- sin(x) Approximation ---")
    print(f"True value (math.sin): {math.sin(test_val)}")
    for n in [2, 5, 10]: # Note: n is the number of terms, not the power
        print(f"Maclaurin (n={n}): {engine.maclaurin_sin(test_val, n)}")