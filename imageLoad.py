import tkinter.filedialog
from PIL import Image
import tkinter

def loadImage() -> Image:
    path: str = tkinter.filedialog.askopenfilename(title="Choose your image",
                                                    filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    image: Image = Image.open(path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image , path