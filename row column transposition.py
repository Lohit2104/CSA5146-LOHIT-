def row_column_encryption(plaintext, key):
    columns = len(key)
    rows = len(plaintext) // columns + (1 if len(plaintext) % columns else 0)
    padding_length = rows * columns - len(plaintext)
    plaintext += 'X' * padding_length
    matrix = [plaintext[i:i + columns] for i in range(0, len(plaintext), columns)]
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    ciphertext = ''.join([''.join([row[i] for row in matrix]) for i in key_order])
    return ciphertext

def row_column_decryption(ciphertext, key):
    columns = len(key)
    rows = len(ciphertext) // columns
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    matrix = [''] * columns
    idx = 0
    for i in key_order:
        matrix[i] = ciphertext[idx:idx + rows]
        idx += rows
    plaintext = ''.join([''.join(row) for row in zip(*matrix)])
    plaintext = plaintext.rstrip('X')
    return plaintext

plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

ciphertext = row_column_encryption(plaintext, key)
decrypted_text = row_column_decryption(ciphertext, key)

print(f"Original Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
