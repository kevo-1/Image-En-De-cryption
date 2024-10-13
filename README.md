# Image-En-De-cryption

<div align=center>
  
![Python](https://img.shields.io/badge/Python-blue?style=flat&logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-red?style=flat&logo=pillow&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-green?style=flat&logo=python&logoColor=white)

</div>

Image-En-De-cryption is a Python project that allows you to encrypt and decrypt images using a logistic map-based algorithm, with plans to incorporate AES encryption in the future. This tool provides an easy-to-use GUI built with Tkinter for selecting, encrypting, and decrypting image files.

## Features

- **Image Encryption**: Encrypt your images using a custom algorithm based on a logistic map.
- **Image Decryption**: Decrypt images that were previously encrypted using the tool.
- **AES Encryption (Upcoming)**: Planned feature to enhance encryption with AES.
- **Tkinter GUI**: A simple graphical interface for selecting and processing images.

## How It Works

1. The user selects an image file using a file dialog.
2. The tool encrypts the image using a logistic map encryption algorithm.
3. The encrypted image is saved in the selected location.
4. The user can also decrypt an encrypted image back to its original form.

## Setup

### Prerequisites

- Python 3.*
- Required libraries: `Pillow`, `Tkinter`, `random`, `math`

To install the dependencies, run:
```bash
pip install pillow
