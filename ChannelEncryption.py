'''
-This encryption method is based on logisitic mapping.
-It uses the equation:
    Xn+1 = r * Xn * (1 - Xn)
-Where r here represents a PI control parameter which is between (3.5, 4)
to ensure it produces chaotic behaviour.
-and Xn when n is intitially equal to zero (zero-based index) has 
to be given a value between (0.5, 1) which is called the current state.
-After generating n-termed sequence where n is the number of pixels of the image
it then multiplies the values of the sequence by 255 which is the max value a channel can withstand
-Then after that is done it uses the bitwise operator XOR between each pixel of the image and
the corresponding value in the sequence and reshapes it in a matrix of the same size of the image
'''

import os
from PIL import Image
from dotenv import load_dotenv
import math

load_dotenv()

#Initial values:
X0: float = float(os.getenv('X0'))
r: float = float(os.getenv('r'))


def LogisticMapping(sizeOfImage: int) -> list[float]:
    Sequence: list[float] = []
    X: float = X0

    for _ in range(sizeOfImage):
        X = r*X*(1-X)
        Sequence.append(X)
    return Sequence


def pixelateSequence(sequence: list[float]) -> list[int]:
    maxPixelVal: int = 255
    resSequence:list[int] = [] 
    for x in sequence:
        temp = int(math.floor(255*x))
        resSequence.append(temp)
    return resSequence


def bitmasking(sequence: list[int], channel: list[int]) -> list[int]:
    final: list[int] = []
    for seqValue, channelPixel in zip(sequence, channel):
        Temp: int = seqValue ^ channelPixel
        final.append(Temp)
    return final


def EncryptChannel(channel: list[int]) -> list[int]:
    sequence: list[float] = LogisticMapping(len(channel))
    sequence = pixelateSequence(sequence=sequence)
    encryptedChannel: list[int] = bitmasking(sequence=sequence, channel=channel)
    return encryptedChannel