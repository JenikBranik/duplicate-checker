import tkinter as tk
from pathlib import Path
from tkinter import filedialog
from src.utils.targetfolder import TargetFolder

def chose_file():
    root = tk.Tk()
    root.withdraw()

    initial_dir = Path.home() / "Downloads"

    path_to_scan = filedialog.askdirectory(initialdir=initial_dir,mustexist=True)
    root.destroy()

    if not path_to_scan:
        raise ValueError("Nothing to do")

    return TargetFolder(path_to_scan)