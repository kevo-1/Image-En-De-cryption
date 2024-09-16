from PIL import Image
from ToolGUI import Window
import tkinter as tk


def main() -> None:
    root = tk.Tk()
    window = Window(root)
    window.run()

if __name__ == '__main__':
    main()