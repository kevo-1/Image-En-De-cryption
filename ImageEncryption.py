import ChannelEncryption
from PIL import Image


def ExtractingChannels(image: Image, channelNum: int, rows:int, columns:int) -> list[int]:
    FinalChannel: list[int] = [image[i ,j][channelNum] for i in range(rows) for j in range(columns)]
    return FinalChannel


def EncryptImage(image: Image) -> Image:
    size = image.size
    rows,columns = size
    image = image.load()
    red = ExtractingChannels(image, 0, rows, columns)
    green = ExtractingChannels(image, 1, rows, columns)
    blue = ExtractingChannels(image, 2, rows, columns)


    encryptedRed = ChannelEncryption.EncryptChannel(channel=red)
    encryptedGreen = ChannelEncryption.EncryptChannel(channel=green)
    encryptedBlue = ChannelEncryption.EncryptChannel(channel=blue)


    Temp = [(r, g, b) for r, g, b in zip(encryptedRed, encryptedGreen, encryptedBlue)]

    EncryptedImage = Image.new('RGB', size)

    pixels = EncryptedImage.load()

    for y in range(EncryptedImage.height):
        for x in range(EncryptedImage.width):
            pixels[x, y] = Temp[EncryptedImage.width*y+x]

    return EncryptedImage

