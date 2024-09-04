def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    seen = set()
    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def format_text(text):
    text = text.upper().replace("J", "I")
    formatted = ""
    prev_char = ""
    for char in text:
        if char.isalpha():
            if char == prev_char:
                formatted += "X"
            formatted += char
            prev_char = char
    if len(formatted) % 2 != 0:
        formatted += "X"
    return formatted

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return (i, row.index(char))

def playfair_cipher(text, key, mode):
    matrix = create_matrix(key)
    text = format_text(text)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            if mode == "encrypt":
                result += matrix[row1][(col1 + 1) % 5]
                result += matrix[row2][(col2 + 1) % 5]
            else:
                result += matrix[row1][(col1 - 1) % 5]
                result += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            if mode == "encrypt":
                result += matrix[(row1 + 1) % 5][col1]
                result += matrix[(row2 + 1) % 5][col2]
            else:
                result += matrix[(row1 - 1) % 5][col1]
                result += matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]
    return result

text = input("Enter the text: ")
key = input("Enter the key: ")
mode = input("Enter mode (encrypt/decrypt): ").lower()

if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode.")
else:
    result = playfair_cipher(text, key, mode)
    print(f"{mode.capitalize()}ed text: {result}")
