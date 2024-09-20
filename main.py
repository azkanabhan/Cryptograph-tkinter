import tkinter as tk
from tkinter import filedialog, messagebox
import vigenere_cipher as vc
import playfair_cipher as pc
import hill_cipher as hc

# Membuat jendela utama
root = tk.Tk()
root.title("Cryptography Tool")
root.geometry("600x800")

# Fungsi untuk memilih file dan membaca isinya
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            input_text.delete("1.0", tk.END)  # Menghapus teks lama di input
            input_text.insert(tk.END, file.read())  # Memasukkan isi file ke input

# Fungsi untuk menyimpan hasil enkripsi/dekripsi ke file
def save_file(content):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(content)

# Fungsi untuk reset input, output, dan kunci
def reset_fields():
    input_text.delete("1.0", tk.END)  # Menghapus teks di input
    output_text.config(state=tk.NORMAL)  # Mengubah output ke state NORMAL untuk bisa dihapus
    output_text.delete("1.0", tk.END)  # Menghapus teks di output
    output_text.config(state=tk.DISABLED)  # Mengubah output kembali ke state DISABLED agar tidak bisa diedit
    key_entry.config(state=tk.NORMAL)  # Membuat input key bisa diedit lagi
    key_entry.delete(0, tk.END)  # Menghapus teks di key_entry

# Fungsi untuk mengatur kunci otomatis ketika metode Hill dipilih
def update_key_entry(*args):
    cipher = cipher_var.get()
    if cipher == "Hill":
        key_entry.delete(0, tk.END)  # Menghapus teks lama di key_entry
        key_entry.insert(0, "GYBNQKURP")  # Memasukkan kunci Hill Cipher
        key_entry.config(state='readonly')  # Membuat key_entry hanya baca (tidak bisa diubah)
    else:
        key_entry.config(state=tk.NORMAL)  # Membuat input key bisa diedit untuk cipher lain
        key_entry.delete(0, tk.END)  # Menghapus teks lama di key_entry jika bukan Hill Cipher

# Frame untuk input dan output
frame = tk.Frame(root)
frame.pack(pady=10)

# Label dan Text Box untuk input
tk.Label(frame, text="Input:").grid(row=0, column=0, padx=5, pady=5)
input_text = tk.Text(frame, height=10, width=60)
input_text.grid(row=0, column=1, padx=5, pady=5)

# Label dan Text Box untuk output
tk.Label(frame, text="Output:").grid(row=1, column=0, padx=5, pady=5)
output_text = tk.Text(frame, height=10, width=60, state=tk.DISABLED)  # Menambahkan state DISABLED
output_text.grid(row=1, column=1, padx=5, pady=5)

# Field untuk memasukkan kunci
tk.Label(root, text="Key (min. 12 chars):").pack(pady=5)
key_entry = tk.Entry(root, width=50)
key_entry.pack(pady=5)

# Tombol untuk memilih file
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=5)

# Tombol untuk menyimpan hasil
save_button = tk.Button(root, text="Save Result", command=lambda: save_file(output_text.get("1.0", tk.END)))
save_button.pack(pady=5)

# Membuat menu dropdown untuk memilih cipher
tk.Label(root, text="Select Encryption Method:").pack(pady=5)
cipher_var = tk.StringVar()
cipher_var.set("Vigenere")  # Default value

cipher_menu = tk.OptionMenu(root, cipher_var, "Vigenere", "Playfair", "Hill")
cipher_menu.pack(pady=5)

# Menghubungkan perubahan cipher_var dengan fungsi update_key_entry
cipher_var.trace("w", update_key_entry)

# Fungsi enkripsi dan dekripsi (akan dihubungkan ke tombol Encrypt dan Decrypt)
def encrypt():
    message = input_text.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    # Tidak ada batasan minimal karakter pada key selain untuk Hill Cipher
    cipher = cipher_var.get()
    try:
        if cipher == "Vigenere":
            result = vc.vigenere_encrypt(message, key)
        elif cipher == "Playfair":
            result = pc.playfair_encrypt(message, key)
        elif cipher == "Hill":
            key_text = "GYBNQKURP"
            def text_to_matrix(text, size=3):
                numbers = [ord(char) - 65 for char in text]
                matrix = [numbers[i:i + size] for i in range(0, len(numbers), size)]
                return matrix

            # Konversi teks kunci ke matriks
            key = text_to_matrix(key_text)
            result = hc.hill_encrypt(message, key)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    output_text.config(state=tk.NORMAL)  # Mengubah output ke state NORMAL agar bisa menampilkan hasil
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state=tk.DISABLED)  # Kembali ke state DISABLED agar tidak bisa diedit
    if cipher != "Hill":
        key_entry.delete(0, tk.END)  # Menghapus teks di key_entry setelah enkripsi untuk selain Hill

def decrypt():
    cipher_text = input_text.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    # Tidak ada batasan minimal karakter pada key selain untuk Hill Cipher
    cipher = cipher_var.get()
    try:
        if cipher == "Vigenere":
            result = vc.vigenere_decrypt(cipher_text, key)
        elif cipher == "Playfair":
            result = pc.playfair_decrypt(cipher_text, key)
        elif cipher == "Hill":
            key_text = "GYBNQKURP"
            def text_to_matrix(text, size=3):
                numbers = [ord(char) - 65 for char in text]
                matrix = [numbers[i:i + size] for i in range(0, len(numbers), size)]
                return matrix

            # Konversi teks kunci ke matriks
            key = text_to_matrix(key_text)
            result = hc.hill_decrypt(cipher_text, key)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    output_text.config(state=tk.NORMAL)  # Mengubah output ke state NORMAL agar bisa menampilkan hasil
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state=tk.DISABLED)  # Kembali ke state DISABLED agar tidak bisa diedit
    if cipher != "Hill":
        key_entry.delete(0, tk.END)  # Menghapus teks di key_entry setelah dekripsi untuk selain Hill

# Tombol untuk enkripsi dan dekripsi
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack(pady=5)

# Tombol untuk reset input dan key
reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.pack(pady=5)

# Menjalankan loop utama
root.mainloop()
