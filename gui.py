import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter.filedialog import askopenfilename
from affine import *
from standardvigenere import *
from fullvigenere import *
from autokeyvigenere import *
from extendedvigenere import *
from playfair import *


class EncryptionMethod:
    @staticmethod
    def affine_cipher(input, key):
        return affineCipher(input, key)

    @staticmethod
    def standard_vigenere(key, input):
        standard = StandardVigenere(key, input)
        return standard.getCipherText()

    @staticmethod
    def full_vigenere(key, input):
        full = FullVigenere(key, input)
        return full.getCipherText()

    @staticmethod
    def autoKey_vigenere(key, input):
        auto = AutoKeyVigenere(key, input)
        return auto.getCipherText()

    @staticmethod
    def extended_vigenere(key, input):
        ext = ExtendedVigenere(key, input)
        return ext.getCipherText()

    @staticmethod
    def playfair_cipher(key, input):
        play = PlayFair(key, input)
        return play.getCipherText()

class DecryptionMethod:
    @staticmethod
    def affine_decipher(input, key):
        return affineDecipher(input, key)

    @staticmethod
    def standard_vigenere(key, input):
        standard = StandardVigenere(key, input)
        return standard.getOriginText()

    @staticmethod
    def full_vigenere(key, input):
        full = FullVigenere(key, input)
        return full.getOriginText()

    @staticmethod
    def autoKey_vigenere(key, input):
        auto = AutoKeyVigenere(key, input)
        return auto.getOriginText()

    @staticmethod
    def extended_vigenere(key, input):
        ext = ExtendedVigenere(key, input)
        return ext.getOriginText()

    @staticmethod
    def playfair_cipher(key, input):
        play = PlayFair(key, input)
        return play.getOriginText()

class UtilityFunction:
    @staticmethod
    def splitText(text):
        listOfChar = [char for char in text]
        stringRes = ''
        for i in listOfChar:
            stringRes += i
        
        return stringRes

    @staticmethod
    def open_file():
        file_path = askopenfilename(filetypes=[('Text Files', '*txt')])
        if file_path is not None:
            pass
        return file_path

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
        self.decrypt_button.configure(command=self.decrypt, state='disabled')

        # import file button
        self.import_button = ttk.Button(sideFrame, text='Import File')
        self.import_button.grid(column=0, row=3, sticky='w', **options)
        self.import_button.configure(command=self.importFile)

        # export file button
        self.export_button = ttk.Button(sideFrame, text='Export File')
        self.export_button.grid(column=1, row=3, sticky='w', **options)
        self.export_button.configure(command=self.exportFile, state='disabled')

        # add padding to the frame and show it
        self.grid(column=0, row=2, padx=5, pady=5, sticky="nsew")

    def encrypt(self, event=None):
        self.encryptText.config(state='normal')
        self.encryptText.delete('1.0', 'end')

        if(self.cipherMethod == 'affine_cipher'):
            input_key1 = int(self.key1_entry.get())
            input_txt = UtilityFunction.splitText(self.inputText.get('1.0', 'end-1c')).lower()
            encrypted = EncryptionMethod.affine_cipher(input_txt, input_key1).upper()
        elif(self.cipherMethod == 'standard_vigenere'):
            input_key1 = self.key1_entry.get()
            input_txt = UtilityFunction.splitText(self.inputText.get('1.0', 'end-1c')).lower()
            encrypted = EncryptionMethod.standard_vigenere(input_key1, input_txt).upper()
        elif(self.cipherMethod == 'full_vigenere'):
            input_key1 = self.key1_entry.get()
            input_txt = UtilityFunction.splitText(self.inputText.get('1.0', 'end-1c')).lower()
            encrypted = EncryptionMethod.full_vigenere(input_key1, input_txt).upper()
        elif(self.cipherMethod == 'autoKey_vigenere'):
            input_key1 = self.key1_entry.get()
            input_txt = UtilityFunction.splitText(self.inputText.get('1.0', 'end-1c')).lower()
            encrypted = EncryptionMethod.autoKey_vigenere(input_key1, input_txt).upper()
        elif(self.cipherMethod == 'extended_vigenere'):
            input_key1 = self.key1_entry.get()
            input_txt = self.inputText.get('1.0', 'end-1c')
            encrypted = EncryptionMethod.extended_vigenere(input_key1, input_txt)
        elif(self.cipherMethod == 'playfair_cipher'):
            input_key1 = self.key1_entry.get()
            input_txt = UtilityFunction.splitText(self.inputText.get('1.0', 'end-1c')).lower()
            encrypted = EncryptionMethod.playfair_cipher(input_key1, input_txt).upper()

        self.encryptText.insert(tk.INSERT, encrypted)
        self.encryptText.config(state='disabled')
        self.export_button.config(state='normal')
        self.decrypt_button.config(state='normal')

    def decrypt(self, event=None):
        self.decryptText.config(state='normal')
        self.decryptText.delete('1.0', 'end')
        
        if(self.cipherMethod == 'affine_cipher'):
            input_txt = self.encryptText.get('1.0', 'end-1c').lower()
            input_key1 = int(self.key1_entry.get())
            decrypted = DecryptionMethod.affine_decipher(input_txt, input_key1).upper()
        elif(self.cipherMethod == 'standard_vigenere'):
            input_txt = self.inputText.get('1.0', 'end-1c').lower()
            input_key1 = self.key1_entry.get()
            decrypted = DecryptionMethod.standard_vigenere(input_key1, input_txt).upper()
        elif(self.cipherMethod == 'full_vigenere'):
            input_txt = self.inputText.get('1.0', 'end-1c').lower()
            input_key1 = self.key1_entry.get()
            decrypted = DecryptionMethod.full_vigenere(input_key1, input_txt).upper()
        elif(self.cipherMethod == 'autoKey_vigenere'):
            input_txt = self.inputText.get('1.0', 'end-1c').lower()
            input_key1 = self.key1_entry.get()
            decrypted = DecryptionMethod.autoKey_vigenere(input_key1, input_txt).upper()
        elif(self.cipherMethod == 'extended_vigenere'):
            input_txt = self.inputText.get('1.0', 'end-1c')
            input_key1 = self.key1_entry.get()
            decrypted = DecryptionMethod.extended_vigenere(input_key1, input_txt)
        elif(self.cipherMethod == 'playfair_cipher'):
            input_txt = self.inputText.get('1.0', 'end-1c').lower()
            input_key1 = self.key1_entry.get()
            decrypted = DecryptionMethod.playfair_cipher(input_key1, input_txt).upper()

        self.decryptText.insert(tk.INSERT, decrypted)
        self.decryptText.config(state='disabled')

    def importFile(self, event=None):
        f = UtilityFunction.open_file()
        readFile = open(f)
        self.inputText.delete('1.0', 'end')
        self.inputText.insert(tk.INSERT, readFile.read())
        print(readFile.read())

    def exportFile(self, event=None):
        self.encryptText.config(state='normal')
        
        encrypt_txt = self.encryptText.get('1.0', 'end-1c')
        filename = 'EncryptedText.txt'
        save_text = open(filename, 'w')
        save_text.write(encrypt_txt)
        save_text.close()

        self.encryptText.config(state='disabled')
        

    def reset(self):
        self.key1_entry.delete(0, "end")
        self.decryptText.config(state='normal')
        self.encryptText.config(state='normal')
        self.decryptText.delete('1.0', 'end')
        self.encryptText.delete('1.0', 'end')
        self.inputText.delete('1.0', 'end')
        self.decryptText.config(state='disabled')
        self.encryptText.config(state='disabled')
        # self.result_label.text = ''


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
            1,
            'standard_vigenere')
        self.frames[2] = ConverterFrame(
            container,
            1,
            'full_vigenere')
        self.frames[3] = ConverterFrame(
            container,
            1,
            'autoKey_vigenere')
        self.frames[4] = ConverterFrame(
            container,
            1,
            'extended_vigenere')
        self.frames[5] = ConverterFrame(
            container,
            1,
            'playfair_cipher')

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