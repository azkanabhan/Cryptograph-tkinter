def generate_key(message, key):
    """
    Menghasilkan kunci yang diperpanjang berdasarkan panjang pesan.
    """
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(message, key):
    """
    Fungsi untuk mengenkripsi pesan menggunakan Vigenere Cipher.
    """
    key = generate_key(message, key)
    cipher_text = []
    for i in range(len(message)):
        if message[i].isalpha():  # hanya mengenkripsi karakter alfabet
            shift = (ord(message[i].upper()) + ord(key[i].upper())) % 26
            cipher_text.append(chr(shift + ord('A')))
        else:
            cipher_text.append(message[i])  # tidak mengenkripsi karakter non-alfabet
    return "".join(cipher_text)

def vigenere_decrypt(cipher_text, key):
    """
    Fungsi untuk mendekripsi pesan menggunakan Vigenere Cipher.
    """
    key = generate_key(cipher_text, key)
    orig_text = []
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():  # hanya mendekripsi karakter alfabet
            shift = (ord(cipher_text[i].upper()) - ord(key[i].upper()) + 26) % 26
            orig_text.append(chr(shift + ord('A')))
        else:
            orig_text.append(cipher_text[i])  # tidak mendekripsi karakter non-alfabet
    return "".join(orig_text)
