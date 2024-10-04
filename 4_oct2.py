import time

# List of sample n values for testing
ns = [1234243, 12342345, 46785687, 3456567]

def testfn(n):
    """Function to evaluate an expression for all values between 0 and n."""
    for i in range(0, n):
        a = i * 10  # Example calculation (you can modify this as needed)

def wrapper(func):
    """Decorator to measure the execution time of a function."""
    def wrapped(*args, **kwargs):  # Accepting *args and **kwargs
        start_time = time.time()  # Start time measurement
        func(*args, **kwargs)      # Call the original function with args and kwargs
        end_time = time.time()     # End time measurement
        
        print(f"For n = {args[0]}, execution time is {end_time - start_time:.6f} seconds")
    
    return wrapped

# Apply the wrapper decorator to the testfn function
@wrapper
def wrapped_testfn(n):
    testfn(n)

# Example usage with different n values
for n in ns:
    wrapped_testfn(n)