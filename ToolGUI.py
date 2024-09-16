import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from imageLoad import loadImage
from PIL import Image, ImageTk
from ImageEncryption import EncryptImage
from ImageDecryption import DecryptImage
import os

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Image En/De-cryption Tool")
        self.root.geometry("1800x800")

        self.frame = tk.Frame(root)
        self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        ####################################################################################################################################################################
        self.encryptPage = tk.Frame(self.frame, background='#bbe6fa')

        #components on the encrypt screen:
        self.image = None
        self.EncryptedImage = None
        self.originalImage = None
        self.encryptedImagePIL = None
        self.originalImagePath = None

        self.encryptionMethods = ttk.Combobox(self.encryptPage, state="readonly", values= ["Logistic Mapping", "AES"])

        self.encryptButton = tk.Button(self.encryptPage, background='white', activebackground='light gray', text= 'encrypt this image', command=self.EncryptLoadedImage)
        self.loadPhoto = tk.Button(self.encryptPage, background='white', activebackground='light gray', text='Choose your image', command= self.useImage)
        self.saveButton = tk.Button(self.encryptPage, background='white', activebackground='light gray', text='save image', command=self.SaveImage)

        self.loadPhoto.place(x= 50, y= 50)

        self.Panel = tk.Label(self.encryptPage, image= self.image)
        self.encryptedPanel = tk.Label(self.encryptPage, image= self.EncryptedImage)

        ####################################################################################################################################################################
        self.decryptPage = tk.Frame(self.frame, background='#a3d6b4')

        #components on the decrypt screen:
        self.image2 = None
        self.DecryptedImage = None
        self.originalImage2 = None
        self.decryptedImagePIL = None
        self.originalImagePath2 = None

        self.decryptButton = tk.Button(self.decryptPage, background='white', activebackground='light gray', text= 'decrypt this image', command=self.DecryptLoadedImage)
        self.loadPhoto2 = tk.Button(self.decryptPage, background='white', activebackground='light gray', text='Choose your image', command= self.useImageDe)
        self.saveButton2 = tk.Button(self.decryptPage, background='white', activebackground='light gray', text='save image', command=self.SaveImageDe)

        self.loadPhoto2.place(x= 50, y= 50)

        self.Panel2 = tk.Label(self.decryptPage, image= self.image2)
        self.decryptedPanel = tk.Label(self.decryptPage, image= self.DecryptedImage)

        ####################################################################################################################################################################

        self.frame2 = tk.Frame(root, background="light gray")
        self.frame2.pack(side=tk.BOTTOM, fill=tk.X)

        self.buttonFrame = tk.Frame(self.frame2, background="light gray")
        self.buttonFrame.pack(side=tk.TOP, pady=10)

        self.EncryptionButton = tk.Button(self.buttonFrame, text='Encrypt', width=10, command=self.showEnPage)
        self.EncryptionButton.grid(row=0, column=0, pady=10, padx=10)
        self.DecryptionButton = tk.Button(self.buttonFrame, text='Decrypt', width=10, command=self.showDePage)
        self.DecryptionButton.grid(row=0, column=1, pady=10, padx=10)

        self.encryptPage.pack(fill=tk.BOTH, expand=True)


    def showEnPage(self) -> None:
        self.encryptPage.pack(fill=tk.BOTH, expand=True)
        self.decryptPage.pack_forget()


    def showDePage(self) -> None:
        self.decryptPage.pack(fill=tk.BOTH, expand=True)
        self.encryptPage.pack_forget()


    def useImage(self):
        temp, self.originalImagePath = loadImage()
        if temp:
            self.originalImage = temp
            maxSize: tuple = (800, 800)
            temp.thumbnail(maxSize)
            self.image: ImageTk = ImageTk.PhotoImage(temp)
            self.Panel.place(x=50, y= 100)
            self.Panel.config(image= self.image)
            self.encryptButton.place(x=200, y=50)
            self.encryptionMethods.place(x=350, y =50)
        else:
            print("No image choosed")


    def useImageDe(self):
        temp, self.originalImagePath2 = loadImage()
        if temp:
            self.originalImage2 = temp
            maxSize: tuple = (800, 800)
            temp.thumbnail(maxSize)
            self.image2: ImageTk = ImageTk.PhotoImage(temp)
            self.Panel2.place(x=50, y= 100)
            self.Panel2.config(image= self.image2)
            self.decryptButton.place(x=200, y=50)
        else:
            print("No image choosed")


    def EncryptLoadedImage(self):
        temp: Image = EncryptImage(self.originalImage)
        if temp:
            self.encryptedImagePIL = temp
            maxSize: tuple = (800, 800)
            temp.thumbnail(maxSize)
            self.EncryptedImage: ImageTk = ImageTk.PhotoImage(temp)
            self.encryptedPanel.place(x=950, y= 100)
            self.encryptedPanel.config(image= self.EncryptedImage)
            self.saveButton.place(x=950, y=50)
        else:
            print("Failed to encrypt")


    def DecryptLoadedImage(self):
        temp: Image = DecryptImage(self.originalImage2)
        if temp:
            self.decryptedImagePIL = temp
            maxSize: tuple = (800, 800)
            temp.thumbnail(maxSize)
            self.DecryptedImage: ImageTk = ImageTk.PhotoImage(temp)
            self.decryptedPanel.place(x=950, y= 100)
            self.decryptedPanel.config(image= self.DecryptedImage)
            self.saveButton2.place(x=950, y=50)
        else:
            print("Failed to decrypt")


    def SaveImage(self):
        defaultName: str = "EncryptedImage.png"
        try:
            originalImageName:str = os.path.basename(self.originalImagePath)
            name,extenstion = os.path.splitext(originalImageName)
            defaultName = f'Encrypted-{name}.png'
        except AttributeError:
            pass

        path: str = filedialog.asksaveasfilename(defaultextension='.png',
                                                initialfile=defaultName,
                                                filetypes=[("*.png", "*.jpg")])
        if path:
            self.encryptedImagePIL.save(path)
        else:
            print("No path choosed!")

    
    def SaveImageDe(self):
        defaultName: str = "DecryptedImage.png"
        try:
            originalImageName:str = os.path.basename(self.originalImagePath2)
            name,extenstion = os.path.splitext(originalImageName)
            defaultName = f'Decrypted-{name}.png'
        except AttributeError:
            pass

        path: str = filedialog.asksaveasfilename(defaultextension='.png',
                                                initialfile=defaultName,
                                                filetypes=[("*.png", "*.jpg")])
        if path:
            self.decryptedImagePIL.save(path)
        else:
            print("No path choosed!")


    def run(self) -> None:
        self.root.mainloop()