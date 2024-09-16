import os
from PIL import Image
from dotenv import load_dotenv
from ChannelEncryption import LogisticMapping
import math

load_dotenv()
# Initial values
X0: float = float(os.getenv('X0'))
r: float = float(os.getenv('r'))

def DecryptImage(image: Image):
    image: Image = image
    size = image.size
    rows, columns = size
    pixels = list(image.getdata())
    
    EncryptedRed: list[int] = []
    EncryptedGreen: list[int] = []
    EncryptedBlue: list[int] = []

    for pixel in pixels:
        r,g,b = pixel
        EncryptedRed.append(r)
        EncryptedGreen.append(g)
        EncryptedBlue.append(b)


    LogisticMap: list[float] = LogisticMapping(rows*columns)
    LogisticMap = [int(math.floor(255*x)) for x in LogisticMap]


    OriginalRed: list[int] = [(x^y) for x,y in zip(LogisticMap, EncryptedRed)]
    OriginalGreen: list[int] = [(x^y) for x,y in zip(LogisticMap, EncryptedGreen)]
    OriginalBlue: list[int] = [(x^y) for x,y in zip(LogisticMap, EncryptedBlue)]

    FinalPixelData: list[tuple] = [(r,g,b) for r,g,b in zip(OriginalRed,OriginalGreen,OriginalBlue)]

    Final: Image = Image.new('RGB', size)
    final_pixels = Final.load()

    for i in range(rows):
        for j in range(columns):
            final_pixels[i, j] = (OriginalRed[i * columns + j],
                                  OriginalGreen[i * columns + j],
                                  OriginalBlue[i * columns + j])

    return Final

