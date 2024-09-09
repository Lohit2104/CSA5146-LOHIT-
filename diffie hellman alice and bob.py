# Original Diffie-Hellman Protocol
def diffie_hellman_protocol(a, q, x, y):
    # Alice sends A = a^x mod q to Bob
    A = pow(a, x, q)
    
    # Bob sends B = a^y mod q to Alice
    B = pow(a, y, q)
    
    # Shared secret key computed by both
    shared_secret_alice = pow(B, x, q)
    shared_secret_bob = pow(A, y, q)
    
    return A, B, shared_secret_alice, shared_secret_bob

# Insecure Protocol (Sending x * a)
def insecure_protocol(a, x, y):
    # Alice sends x * a to Bob
    A_insecure = x * a
    
    # Bob sends y * a to Alice
    B_insecure = y * a
    
    return A_insecure, B_insecure

# User input
a = int(input("Enter the public base (a): "))
q = int(input("Enter the prime modulus (q): "))
x = int(input("Alice's secret number (x): "))
y = int(input("Bob's secret number (y): "))

# Original Diffie-Hellman Protocol
A, B, shared_secret_alice, shared_secret_bob = diffie_hellman_protocol(a, q, x, y)

print("\nOriginal Diffie-Hellman Protocol:")
print(f"Alice sends: A = {A}")
print(f"Bob sends: B = {B}")
print(f"Shared secret computed by Alice: {shared_secret_alice}")
print(f"Shared secret computed by Bob: {shared_secret_bob}")

# Insecure Protocol
A_insecure, B_insecure = insecure_protocol(a, x, y)

print("\nInsecure Protocol (sending x * a):")
print(f"Alice sends: {A_insecure}")
print(f"Bob sends: {B_insecure}")

# Eve's attack on the insecure protocol
eve_finds_x = A_insecure // a
eve_finds_y = B_insecure // a

print("\nEve's Attack on the Insecure Protocol:")
print(f"Eve finds Alice's secret number: {eve_finds_x}")
print(f"Eve finds Bob's secret number: {eve_finds_y}")
