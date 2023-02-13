import tkinter as tk
from tkinter import Button
from tkinter import filedialog
import rsa

def encrypt_file(file_path, public_key_path):
    with open(file_path, "rb") as f:
        data = f.read()
    with open(public_key_path, "rb") as f:
        pubkey = rsa.PublicKey.load_pkcs1(f.read())
    encrypted_data = rsa.encrypt(data, pubkey)
    with open(file_path + ".enc", "wb") as f:
        f.write(encrypted_data)

def decrypt_file(file_path, private_key_path):
    with open(file_path, "rb") as f:
        data = f.read()
    with open(private_key_path, "rb") as f:
        privkey = rsa.PrivateKey.load_pkcs1(f.read())
    decrypted_data = rsa.decrypt(data, privkey)
    with open(file_path + ".dec", "wb") as f:
        f.write(decrypted_data)

def generate_key_pair(bits, public_key_path, private_key_path):
    (pubkey, privkey) = rsa.newkeys(bits)
    with open(public_key_path, "wb") as f:
        f.write(pubkey.save_pkcs1())
    with open(private_key_path, "wb") as f:
        f.write(privkey.save_pkcs1())

def open_file():
    # اختيار الملف المراد تشفيره أو فك تشفيره
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def select_public_key():
    # اختيار المفتاح العام المستخدم لتشفير الملف
    public_key_path = filedialog.askopenfilename()
    public_key_entry.delete(0, tk.END)
    public_key_entry.insert(0, public_key_path)

def select_private_key():
    # اختيار المفتاح الخاص المستخدم لفك تشفير الملف
    private_key_path = filedialog.askopenfilename()
    private_key_entry.delete(0, tk.END)
    private_key_entry.insert(0, private_key_path)

def select_key_size():
    # اختيار طول مفتاح RSA
    key_size = key_size_var.get()
    key_size_label.config(text=f"Key Size: {key_size}")

def encrypt():
    # تشفير الملف باستخدام المفتاح العام المحدد
    file_path = file_entry.get()
    public_key_path = public_key_entry.get()
    encrypt_file(file_path, public_key_path)
    result_label.config(text="File encrypted successfully")

def decrypt():
    # فك تشفير الملف باستخدام المفتاح الخاص المحدد
    file_path = file_entry.get()
    private_key_path = private_key_entry.get()
    decrypt_file(file_path, private_key_path)
    result_label.config(text="File decrypted successfully")

def generate_keys():
    # إنشاء مفاتيح جديدة بناءً على الطول المحدد
    bits = key_size_var.get()
    public_key_path = public_key_entry.get()
    private_key_path = private_key_entry.get()
    generate_key_pair(bits, public_key_path,     private_key_path)
    result_label.config(text="Key pair generated successfully")

root = tk.Tk()
root.title("binary_cryptor_rsa by Dragon-Noir2023 ")
root.geometry("400x400")

main_frame = tk.Frame(root)
main_frame.pack()

file_label = tk.Label(main_frame, text="File:")
file_label.grid(row=0, column=0)
file_entry = tk.Entry(main_frame)
file_entry.grid(row=0, column=1)
file_button = tk.Button(main_frame, text="Open", command=open_file)
file_button.grid(row=0, column=2)

encrypt_button = tk.Button(main_frame, text="Encrypt", command=encrypt)
encrypt_button.grid(row=3, column=0)

decrypt_button = tk.Button(main_frame, text="Decrypt", command=decrypt)
decrypt_button.grid(row=3, column=1)

key_size_label = tk.Label(main_frame, text="Key Size: 1024")
key_size_label.grid(row=4, column=0)
key_size_var = tk.IntVar(value=1024)
key_size_menu = tk.OptionMenu(main_frame, key_size_var, 512, 1024, 2048, command=select_key_size)
key_size_menu.grid(row=4, column=1)

generate_keys_button = tk.Button(main_frame, text="Generate Keys", command=generate_keys)
generate_keys_button.grid(row=4, column=2)

public_key_label = tk.Label(main_frame, text="Public Key:")
public_key_label.grid(row=1, column=0)
public_key_entry = tk.Entry(main_frame)
public_key_entry.grid(row=1, column=1)
public_key_button = tk.Button(main_frame, text="Select", command=select_public_key)
public_key_button.grid(row=1, column=2)

private_key_label = tk.Label(main_frame, text="Private Key:")
private_key_label.grid(row=2, column=0)
private_key_entry = tk.Entry(main_frame)
private_key_entry.grid(row=2, column=1)
private_key_button = tk.Button(main_frame, text="Select", command=select_private_key)
private_key_button.grid(row=2, column=2)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()