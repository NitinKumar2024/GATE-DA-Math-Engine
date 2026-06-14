class CalculusEngine:
    def __init__(self, tolerance=1e-2, h=1e-5):
        self.tolerance = tolerance  # Used for checking equality
        self.h = h                  # Used for taking microscopic steps

    def get_limits(self, func, c):
        """Returns the Left-Hand and Right-Hand limits as a tuple (LHL, RHL)"""
        # Approximate limits
        LHL = func(c - self.tolerance)
        RHL = func(c + self.tolerance)
        return (LHL, RHL)
        

    def is_continuous(self, func, c):
        """Returns True if continuous, False otherwise. (Watch out for ZeroDivisionError)"""
        try:
            f_c = func(c)
        except ZeroDivisionError:
            return False # Fails Step 1: The Target does not exist
    
        try:
            # Approximate limits
            LHL, RHL = self.get_limits(func, c)
            
            # Step 4 & 5: Check if LHL == RHL == f(c) using absolute floating-point tolerance
            if abs(LHL - RHL) < 1e-2 and abs(LHL - f_c) < 1e-2:
                return True
            else:
                return False
        except ZeroDivisionError:
            return False
    

    def is_differentiable(self, func, c):
        """Returns True if continuous AND smooth, False otherwise."""
        # Step 1: The Hierarchy Law. If it's broken, it can't be smooth.
        if not self.is_continuous(func, c):
            return False
            
        # Step 2: Calculate Left-Hand Slope (stepping backward)
        LHD = (func(c) - func(c - self.h)) / self.h
        
        # Step 3: Calculate Right-Hand Slope (stepping forward)
        RHD = (func(c + self.h) - func(c)) / self.h
        
        # Step 4: The Collision Check. Do the slopes match?
        if abs(LHD - RHD) < self.tolerance:
            return True
        else:
            return False
        

# --- THE CRUCIBLE TESTING SUITE ---

def f1(x):
    return x**2  # Smooth parabola

def f2(x):
    return abs(x - 3)  # Sharp corner at x=3

def f3(x):
    return (x**2 - 4) / (x - 2) # Missing brick at x=2

if __name__ == "__main__":
    engine = CalculusEngine()
    
    print("--- Diagnostics Report ---")
    print(f"f1 at x=2 -> Continuous: {engine.is_continuous(f1, 2)}, Differentiable: {engine.is_differentiable(f1, 2)}")
    print(f"f2 at x=3 -> Continuous: {engine.is_continuous(f2, 3)}, Differentiable: {engine.is_differentiable(f2, 3)}")
    print(f"f3 at x=2 -> Continuous: {engine.is_continuous(f3, 2)}, Differentiable: {engine.is_differentiable(f3, 2)}")