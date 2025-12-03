import os
import tkinter as tk
from tkinter import filedialog

def chose_file():
    chosen_file = os.path.join(os.path.expanduser("~"), "Downloads")
    root = tk.Tk()
    root.withdraw()

    inputFile = filedialog.askopenfilename(
        title="Chose file to scan",
        initialdir=chosen_file
    )
    return inputFile
