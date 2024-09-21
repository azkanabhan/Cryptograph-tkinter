# Cryptography Tool

Cryptography Tool adalah sebuah aplikasi berbasis GUI yang dibuat menggunakan Python dan Tkinter. Aplikasi ini mendukung beberapa metode enkripsi dan dekripsi termasuk Vigenere Cipher, Playfair Cipher, dan Hill Cipher.

## Fitur
- **Vigenere Cipher**: Mendukung enkripsi dan dekripsi dengan panjang kunci berapa pun.
- **Playfair Cipher**: Mendukung enkripsi dan dekripsi dengan kunci minimal 5 karakter.
- **Hill Cipher**: Mendukung enkripsi dan dekripsi dengan kunci khusus yang menghasilkan matriks kunci yang valid.

## Prasyarat
Pastikan Anda telah menginstal Python 3.x di sistem Anda. Anda juga perlu menginstal pustaka `numpy` untuk Hill Cipher.

### Instalasi `numpy`
```bash
   pip install numpy
```

# Penggunaan

1. **Buka aplikasi** dengan menjalankan `main.py`.
2. **Masukkan pesan** yang ingin dienkripsi atau didekripsi di bagian **Input**.
3. **Pilih metode enkripsi/dekripsi** dari menu dropdown:
   - **Vigenere**: Dapat menggunakan kunci dengan panjang berapa pun. Pastikan kunci hanya mengandung huruf.
   - **Playfair**: Menggunakan kunci minimal 5 karakter. Kunci secara otomatis mengganti `J` dengan `I`.
   - **Hill**: Otomatis mengatur kunci menjadi `GYBNQKURP` dan tidak dapat diubah.
4. **Masukkan kunci enkripsi** di bagian **Key**.
5. Klik tombol **Encrypt** untuk mengenkripsi atau **Decrypt** untuk mendekripsi pesan.
6. Hasil enkripsi atau dekripsi akan ditampilkan di bagian **Output**.
7. Anda dapat menyimpan hasil enkripsi atau dekripsi menggunakan tombol **Save Result**.

# Peringatan

## Vigenere Cipher
- Pastikan kunci hanya berisi huruf. Kunci dengan karakter non-huruf akan menyebabkan kesalahan.

## Playfair Cipher
- Saat mengenkripsi atau mendekripsi, karakter `J` dalam pesan akan diubah menjadi `I`.
- Jika ada dua huruf yang sama dalam pasangan (misalnya "LL"), sebuah `X` akan disisipkan di antara mereka.

## Hill Cipher
- Saat memilih metode Hill Cipher, kunci otomatis diatur menjadi `GYBNQKURP` (3x3 matriks kunci). Ini memastikan enkripsi dan dekripsi berjalan dengan benar.
- **Penting**: Hill Cipher membutuhkan kunci yang menghasilkan matriks kunci yang valid. Matriks harus memiliki determinan yang tidak nol dan memiliki invers dalam modulus 26. Tidak semua kunci dapat menghasilkan matriks yang valid.
- Jika Anda mencoba menggunakan kunci Hill Cipher lain, pastikan panjangnya 9 karakter (3x3 matriks) atau 16 karakter (4x4 matriks) dan menghasilkan matriks kunci yang valid.

# Masalah yang Sering Ditemui

- **Error Import**: Jika `numpy` tidak diinstal, aplikasi tidak akan berjalan dengan benar untuk Hill Cipher. Pastikan Anda telah menginstal `numpy`.
- **Key Invalid**: Jika kunci untuk Hill Cipher tidak valid, Anda akan menerima pesan kesalahan. Gunakan kunci default `GYBNQKURP` untuk memastikan operasi berjalan dengan benar.
