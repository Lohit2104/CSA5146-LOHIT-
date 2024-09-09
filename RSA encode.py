import math

# Function to find gcd of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to factor n using the gcd approach if we know a plaintext block
def factor_n_with_plaintext(n, m):
    # Calculate gcd of plaintext block m and n
    factor = gcd(m, n)
    
    if factor > 1 and factor < n:  # A non-trivial factor of n was found
        p = factor
        q = n // p  # The other factor
        print(f"Found factors of n: p = {p}, q = {q}")
        return p, q
    else:
        print("No non-trivial factors found.")
        return None, None

# User input
n = int(input("Enter the value of n (product of two primes p and q): "))
m = int(input("Enter a plaintext block m: "))

# Try to factor n using the plaintext block
p, q = factor_n_with_plaintext(n, m)

if p and q:
    print("n has been factored successfully.")
else:
    print("Unable to factor n using the provided plaintext block.")
