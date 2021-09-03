import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from affine import *


class EncryptionMethod:
    @staticmethod
    def affine_cipher(input, key):
        return affineCipher(input, key)

class DecryptionMethod:
    @staticmethod
    def affine_decipher(input, key):
        return affineDecipher(input, key)

class ConverterFrame(ttk.Frame):
    def __init__(self, container, keyTotal, cipherMethod):
        super().__init__(container)

        self.keyTotal = keyTotal
        self.cipherMethod = cipherMethod

        # field options
        options = {'padx': 5, 'pady': 0}

        self.inputLabel = ttk.Label(self, text='Input Text')
        self.inputLabel.grid(column=0, row=0, sticky='w', **options)
        self.inputText = tk.Text(self, height=25, width=30)
        self.inputText.grid(column=0, row=1, **options)

        self.encryptLabel = ttk.Label(self, text='Encrypted Text')
        self.encryptLabel.grid(column=1, row=0, sticky='w', **options)
        self.encryptText = tk.Text(self, height=25, width=30, state='disabled')
        self.encryptText.grid(column=1, row=1, **options)

        self.decryptLabel = ttk.Label(self, text='Decrypted Text')
        self.decryptLabel.grid(column=2, row=0, sticky='w', **options)
        self.decryptText = tk.Text(self, height=25, width=30, state='disabled')
        self.decryptText.grid(column=2, row=1, **options)

        # field options
        options = {'padx': 5, 'pady': 5}

        sideFrame = tk.Frame(self, padx=25, pady=15)
        sideFrame.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

        # key1 label
        self.key1_label = ttk.Label(sideFrame, text='Key 1')
        self.key1_label.grid(column=0, row=0, sticky='n',  **options)

        # key1 entry
        self.key1 = tk.StringVar()
        self.key1_entry = ttk.Entry(sideFrame, textvariable=self.key1)
        self.key1_entry.grid(column=1, row=0, sticky='n', **options)
        self.key1_entry.focus()

        if(self.keyTotal==2):
            # key2 label
            self.key2_label = ttk.Label(sideFrame, text='Key 2')
            self.key2_label.grid(column=0, row=1, sticky='n',  **options)

            # key2 entry
            self.key2 = tk.StringVar()
            self.key2_entry = ttk.Entry(sideFrame, textvariable=self.key2)
            self.key2_entry.grid(column=1, row=1, sticky='n', **options)
            self.key2_entry.focus()

        # encrypt button
        self.encrypt_button = ttk.Button(sideFrame, text='Encrypt Text')
        self.encrypt_button.grid(column=0, row=2, sticky='w', **options)
        self.encrypt_button.configure(command=self.encrypt)

        # decrypt button
        self.decrypt_button = ttk.Button(sideFrame, text='Decrypt Text')
        self.decrypt_button.grid(column=1, row=2, sticky='w', **options)
        self.decrypt_button.configure(command=self.decrypt)

        # import file button
        self.import_button = ttk.Button(sideFrame, text='Import File')
        self.import_button.grid(column=0, row=3, sticky='w', **options)

        # export file button
        self.export_button = ttk.Button(sideFrame, text='Export File')
        self.export_button.grid(column=1, row=3, sticky='w', **options)

        # result label
        self.result_label = ttk.Label(sideFrame)
        self.result_label.grid(row=5, columnspan=3, **options)

        # add padding to the frame and show it
        self.grid(column=0, row=2, padx=5, pady=5, sticky="nsew")

    def encrypt(self, event=None):
        self.encryptText.config(state='normal')
        self.encryptText.delete('1.0', 'end')

        input_txt = self.inputText.get('1.0', 'end')
        input_key1 = int(self.key1_entry.get())

        if(self.cipherMethod == 'affine_cipher'):
            encrypted = EncryptionMethod.affine_cipher(input_txt, input_key1)

        self.encryptText.insert(tk.INSERT, encrypted)
        self.encryptText.config(state='disabled')

    def decrypt(self, event=None):
        self.decryptText.config(state='normal')
        self.decryptText.delete('1.0', 'end')

        input_txt = self.encryptText.get('1.0', 'end-1c')
        input_key1 = int(self.key1_entry.get())
        
        if(self.cipherMethod == 'affine_cipher'):
            decrypted = DecryptionMethod.affine_decipher(input_txt, input_key1)

        self.decryptText.insert(tk.INSERT, decrypted)
        self.decryptText.config(state='disabled')

    def reset(self):
        self.key1_entry.delete(0, "end")
        self.decryptText.config(state='normal')
        self.encryptText.config(state='normal')
        self.decryptText.delete('1.0', 'end')
        self.encryptText.delete('1.0', 'end')
        self.inputText.delete('1.0', 'end')
        self.decryptText.config(state='disabled')
        self.encryptText.config(state='disabled')
        self.result_label.text = ''


class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):

        super().__init__(container)
        self['text'] = 'Options'

        # radio buttons
        self.selected_value = tk.IntVar()

        ttk.Radiobutton(
            self,
            text='Affine Cipher',
            value=0,
            variable=self.selected_value,
            command=self.change_frame).grid(column=0, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text='Standard Vigenere Cipher',
            value=1,
            variable=self.selected_value,
            command=self.change_frame).grid(column=1, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text='Full Vigenere Cipher',
            value=2,
            variable=self.selected_value,
            command=self.change_frame).grid(column=2, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text='Auto-key Vigenere Cipher',
            value=3,
            variable=self.selected_value,
            command=self.change_frame).grid(column=3, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text='Extended Vigenere Cipher',
            value=4,
            variable=self.selected_value,
            command=self.change_frame).grid(column=4, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text='Playfair Cipher',
            value=5,
            variable=self.selected_value,
            command=self.change_frame).grid(column=5, row=0, padx=5, pady=5)

        self.grid(column=0, row=1, padx=5, pady=5, sticky='ew')

        # initialize frames
        self.frames = {}
        self.frames[0] = ConverterFrame(
            container,
            1,
            'affine_cipher')
        self.frames[1] = ConverterFrame(
            container,
            2,
            'affine_cipher')

        self.change_frame()

    def change_frame(self):
        frame = self.frames[self.selected_value.get()]
        frame.reset()
        frame.tkraise()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tugas 1 Kripto")
        self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    ControlFrame(app)
    app.mainloop()