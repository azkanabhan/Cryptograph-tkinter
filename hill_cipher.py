import numpy as np

def mod_inverse(a, m):
    """
    Menghitung invers modul dari a terhadap m menggunakan metode extended Euclidean.
    Mengembalikan None jika tidak ada invers.
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def generate_key_matrix_from_list(key_list):
    """
    Menghasilkan matriks kunci dari list angka yang diberikan.
    """
    size = len(key_list)
    key_matrix = np.array(key_list).reshape(size, size)
    return key_matrix

def hill_encrypt(plaintext, key):
    """
    Fungsi untuk mengenkripsi pesan menggunakan Hill Cipher.
    """
    n = len(key)
    plaintext = plaintext.upper().replace(" ", "")
    
    # Tambahkan padding 'X' jika panjang plaintext tidak sesuai ukuran matriks
    while len(plaintext) % n != 0:
        plaintext += 'X'
    
    # Ubah plaintext menjadi vektor angka
    plaintext_vector = [ord(char) - 65 for char in plaintext]
    
    # Ubah plaintext menjadi matriks
    plaintext_matrix = np.array(plaintext_vector).reshape(-1, n)
    key_matrix = generate_key_matrix_from_list(key)
    
    # Enkripsi: (plaintext_matrix * key_matrix) mod 26
    ciphertext_matrix = (np.dot(plaintext_matrix, key_matrix) % 26).astype(int)
    
    # Ubah matriks hasil enkripsi menjadi teks
    ciphertext = ''.join([chr(num + 65) for num in ciphertext_matrix.flatten()])
    return ciphertext

def hill_decrypt(ciphertext, key):
    """
    Fungsi untuk mendekripsi pesan menggunakan Hill Cipher.
    """
    n = len(key)
    ciphertext = ciphertext.upper().replace(" ", "")
    
    # Ubah ciphertext menjadi vektor angka
    ciphertext_vector = [ord(char) - 65 for char in ciphertext]
    
    # Ubah ciphertext menjadi matriks
    ciphertext_matrix = np.array(ciphertext_vector).reshape(-1, n)
    key_matrix = generate_key_matrix_from_list(key)
    
    # Hitung determinan dan invers determinan
    determinant = int(round(np.linalg.det(key_matrix)))
    determinant_inv = mod_inverse(determinant, 26)
    if determinant_inv is None:
        raise ValueError("Matriks kunci tidak memiliki invers. Dekripsi tidak bisa dilakukan.")
    
    # Menghitung matriks adjugate
    adjugate_matrix = np.round(np.linalg.inv(key_matrix) * determinant).astype(int) % 26
    
    # Hitung invers dari matriks kunci dalam modulus 26
    key_inverse = (determinant_inv * adjugate_matrix) % 26
    
    # Dekripsi: (ciphertext_matrix * key_inverse) mod 26
    plaintext_matrix = (np.dot(ciphertext_matrix, key_inverse) % 26).astype(int)
    
    # Ubah matriks hasil dekripsi menjadi teks
    plaintext = ''.join([chr(num + 65) for num in plaintext_matrix.flatten()])
    
    # Menghapus padding 'X' yang tidak diperlukan
    plaintext = plaintext.rstrip('X')
    return plaintext


