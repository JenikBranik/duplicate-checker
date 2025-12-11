import tkinter as tk
from pathlib import Path
from tkinter import filedialog
from src.utils.targetfolder import TargetFolder

def chose_folders() -> list[TargetFolder] :
    """
    A method based on the tkinter library that
    invokes a filedialog for folder selection
    :return:
    """
    folders = []
    seen_paths = set()
    root = tk.Tk()
    root.withdraw()

    initial_dir = Path.home() / "Downloads"

    while True:
        path_to_scan = filedialog.askdirectory(initialdir=initial_dir,mustexist=True)

        if not path_to_scan:
            break

        if not path_to_scan in seen_paths:
            seen_paths.add(path_to_scan)
            folders.append(TargetFolder(path_to_scan))
        else:
            raise ValueError("Error")

        if not path_to_scan:
            raise ValueError("Nothing to do")

    if len(folders) == 0:
        raise ValueError("No folders selected")

    return folders