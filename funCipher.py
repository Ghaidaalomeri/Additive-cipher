import tkinter as tk

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plaintext, key):
    plaintext = plaintext.lower()
    encryptedText = []
    for i in range(len(plaintext)):  
        if plaintext[i] != " ":
            indexing = alphabet.index(plaintext[i])
            cipherAlgo = (indexing + int(key)) % 26
            new = alphabet[cipherAlgo]
            encryptedText.append(new)
    return "".join(encryptedText)  

def decrypt(decrypttext, key):
    decrypttext = decrypttext.lower()
    decryptedText = []
    for i in range(len(decrypttext)):
        if decrypttext[i] != " ":
            indexing = (alphabet.index(decrypttext[i]))
            x = indexing - int(key)
            if x >= 0:
                cipherAlgo = (indexing - int(key)) % 26
                shifter = alphabet[cipherAlgo]
                decryptedText.append(shifter)
            else:
                cipherAlgo = (indexing - int(key)) + 26
                shifter = alphabet[cipherAlgo]
                decryptedText.append(shifter)
    return "".join(decryptedText)

def cryptanalysis(plaintext, ciphertext):
    plaintext = plaintext.lower()
    ciphertext = ciphertext.lower()
    if len(plaintext) != len(ciphertext):
        return "Error: Plaintext and ciphertext must be the same length."
    else:
        for i in range(len(plaintext)):  
            p = plaintext[i]
            c = ciphertext[i]
            if p in alphabet and c in alphabet:  
                key = (alphabet.index(c) - alphabet.index(p)) % 26
                return key

def on_encrypt():
    plaintext = entry_plaintext.get()
    key = entry_key.get()
    encrypted_text = encrypt(plaintext, key)
    label_result.config(text=f"Encrypted text: {encrypted_text}")

def on_decrypt():
    ciphertext = entry_plaintext.get()
    key = entry_key.get()
    decrypted_text = decrypt(ciphertext, key)
    label_result.config(text=f"Decrypted text: {decrypted_text}")

def on_cryptanalysis():
    plaintext = entry_plaintext.get()
    ciphertext = entry_ciphertext.get()
    key = cryptanalysis(plaintext, ciphertext)
    if isinstance(key, int):
        label_result.config(text=f"Key found: {key}")
    else:
        label_result.config(text=key)

# Create the main window
root = tk.Tk()
root.title("Cryptosystem")

# Set the background color and window size
root.config(bg='white')
root.geometry("500x400")

# Labels and input fields
label_plaintext = tk.Label(root, text="Enter text:", bg='white')
label_plaintext.pack(pady=5)

entry_plaintext = tk.Entry(root, width=50)
entry_plaintext.pack(pady=5)

label_ciphertext = tk.Label(root, text="Enter ciphertext (for cryptanalysis):", bg='white')
label_ciphertext.pack(pady=5)

entry_ciphertext = tk.Entry(root, width=50)
entry_ciphertext.pack(pady=5)

label_key = tk.Label(root, text="Enter key:", bg='white')
label_key.pack(pady=5)

entry_key = tk.Entry(root, width=50)
entry_key.pack(pady=5)

# Buttons
button_encrypt = tk.Button(root, text="Encrypt", command=on_encrypt, bg='navy', fg='white', width=20)
button_encrypt.pack(pady=5)

button_decrypt = tk.Button(root, text="Decrypt", command=on_decrypt, bg='navy', fg='white', width=20)
button_decrypt.pack(pady=5)

button_cryptanalysis = tk.Button(root, text="Cryptanalysis", command=on_cryptanalysis, bg='navy', fg='white', width=20)
button_cryptanalysis.pack(pady=5)

# Result label
label_result = tk.Label(root, text="", bg='white')
label_result.pack(pady=10)

# Run the GUI
root.mainloop()
