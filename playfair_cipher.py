def generate_playfair_matrix(key):
    """
    Menghasilkan matriks 5x5 untuk Playfair Cipher berdasarkan kunci.
    """
    matrix = []
    key = key.upper().replace("J", "I").replace(" ", "")  # Ganti 'J' dengan 'I'
    used_chars = set()

    # Menambahkan karakter kunci ke matriks
    for char in key:
        if char not in used_chars and char.isalpha():
            matrix.append(char)
            used_chars.add(char)

    # Menambahkan karakter yang tersisa (tanpa 'J')
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used_chars:
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def prepare_message(message):
    """
    Memformat pesan untuk Playfair Cipher: mengubah menjadi uppercase, mengganti 'J' dengan 'I',
    dan menambahkan padding 'X' jika diperlukan.
    """
    message = message.upper().replace("J", "I").replace(" ", "")
    formatted_message = ""
    i = 0
    while i < len(message):
        # Jika karakter terakhir tidak memiliki pasangan, tambahkan 'X'
        if i == len(message) - 1:
            formatted_message += message[i] + 'X'
            i += 1
        # Jika dua karakter berurutan sama, tambahkan 'X' di antaranya
        elif message[i] == message[i + 1]:
            formatted_message += message[i] + 'X'
            i += 1
        else:
            formatted_message += message[i] + message[i + 1]
            i += 2

    return formatted_message

def find_position(matrix, char):
    """
    Mencari posisi karakter dalam matriks.
    """
    for i, row in enumerate(matrix):
        for j, matrix_char in enumerate(row):
            if matrix_char == char:
                return i, j
    return None

def playfair_encrypt(message, key):
    """
    Fungsi untuk mengenkripsi pesan menggunakan Playfair Cipher.
    """
    matrix = generate_playfair_matrix(key)
    message = prepare_message(message)  # Format pesan sebelum enkripsi
    encrypted_message = []

    for i in range(0, len(message), 2):
        char1, char2 = message[i], message[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:  # Huruf dalam baris yang sama
            encrypted_message.append(matrix[row1][(col1 + 1) % 5])
            encrypted_message.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:  # Huruf dalam kolom yang sama
            encrypted_message.append(matrix[(row1 + 1) % 5][col1])
            encrypted_message.append(matrix[(row2 + 1) % 5][col2])
        else:  # Huruf dalam baris dan kolom yang berbeda
            encrypted_message.append(matrix[row1][col2])
            encrypted_message.append(matrix[row2][col1])

    return "".join(encrypted_message)

def playfair_decrypt(cipher_text, key):
    """
    Fungsi untuk mendekripsi pesan menggunakan Playfair Cipher.
    """
    matrix = generate_playfair_matrix(key)
    decrypted_message = []

    for i in range(0, len(cipher_text), 2):
        char1, char2 = cipher_text[i], cipher_text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:  # Huruf dalam baris yang sama
            decrypted_message.append(matrix[row1][(col1 - 1) % 5])
            decrypted_message.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:  # Huruf dalam kolom yang sama
            decrypted_message.append(matrix[(row1 - 1) % 5][col1])
            decrypted_message.append(matrix[(row2 - 1) % 5][col2])
        else:  # Huruf dalam baris dan kolom yang berbeda
            decrypted_message.append(matrix[row1][col2])
            decrypted_message.append(matrix[row2][col1])

    # Menghapus padding 'X' yang ditambahkan di antara huruf yang berulang atau di akhir pesan
    decrypted_message = "".join(decrypted_message)
    cleaned_message = ""
    i = 0
    while i < len(decrypted_message):
        # Menghapus 'X' yang digunakan sebagai padding
        if i < len(decrypted_message) - 1 and decrypted_message[i] == 'X':
            if decrypted_message[i - 1] == decrypted_message[i + 1]:
                i += 1  # Lewati 'X' yang tidak diperlukan
            else:
                cleaned_message += decrypted_message[i]
        else:
            cleaned_message += decrypted_message[i]
        i += 1

    return cleaned_message
