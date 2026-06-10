def check_continuity(func, c, tolerance=1e-4):
    try:
        f_c = func(c)
    except ZeroDivisionError:
        return False # Fails Step 1: The Target does not exist
    
    try:
        # Approximate limits
        LHL = func(c - tolerance)
        RHL = func(c + tolerance)
        
        # Step 4 & 5: Check if LHL == RHL == f(c) using absolute floating-point tolerance
        if abs(LHL - RHL) < 1e-2 and abs(LHL - f_c) < 1e-2:
            return True
        else:
            return False
    except ZeroDivisionError:
        return False
    
    

# Test your code:
def test_func(x):
    if x < 4:
        return (x**0.5 - 2) / (x - 4)
    else:
        # Assuming you found c = 0 in the math crucible:
        return 0 * x + 0.25

print(check_continuity(test_func, 4)) # Should output True if your 'c' is correct