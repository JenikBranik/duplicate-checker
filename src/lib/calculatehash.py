import hashlib
from pathlib import Path

def calculate_hash(file_path: Path, chunk_size=4096) -> str:
    """
    Calculate the hash of a file.
    :param file_path: Instance cotaining the path
    :param chunk_size: Size of data chunsk read
    :return: SHA256 hash of the file
    """
    hasher = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()
    except OSError:
        raise OSError("File error")