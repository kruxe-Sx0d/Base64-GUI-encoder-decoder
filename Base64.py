import tkinter as tk
from tkinter import messagebox
import base64


class SimpleCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Encrypt/Decrypt")
        self.root.geometry("450x350")

        self.label = tk.Label(root, text="Enter text:")
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.pack(pady=5)

        self.encrypt_btn = tk.Button(
            root, text="Encrypt", command=self.encrypt)
        self.encrypt_btn.pack(pady=5)

        self.decrypt_btn = tk.Button(
            root, text="Decrypt", command=self.decrypt)
        self.decrypt_btn.pack(pady=5)

        self.copy_btn = tk.Button(
            root, text="Copy Output", command=self.copy_output)
        self.copy_btn.pack(pady=5)

        self.clear_btn = tk.Button(root, text="Clear", command=self.clear)
        self.clear_btn.pack(pady=5)

        self.output_label = tk.Label(root, text="", fg="blue", wraplength=400)
        self.output_label.pack(pady=20)

    def encrypt(self):
        text = self.text_entry.get()
        if text:
            # Encode text to bytes, then to base64
            encoded_bytes = base64.b64encode(text.encode('utf-8'))
            encrypted = encoded_bytes.decode('utf-8')
            self.output_label.config(text=f"Encrypted: {encrypted}")
        else:
            messagebox.showinfo("Info", "Please enter some text!")

    def decrypt(self):
        text = self.text_entry.get()
        if text:
            try:
                decoded_bytes = base64.b64decode(text.encode('utf-8'))
                decrypted = decoded_bytes.decode('utf-8')
                self.output_label.config(text=f"Decrypted: {decrypted}")
            except Exception:
                messagebox.showerror("Error", "Invalid encrypted text!")
        else:
            messagebox.showinfo("Info", "Please enter some text!")

    def copy_output(self):
        output = self.output_label.cget("text")
        if output:
            self.root.clipboard_clear()
            self.root.clipboard_append(output.split(":", 1)[1].strip())
            messagebox.showinfo("Copied", "Output copied to clipboard!")
        else:
            messagebox.showinfo("Info", "No output to copy!")

    def clear(self):
        self.text_entry.delete(0, tk.END)
        self.output_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCipherApp(root)
    root.mainloop()
