from collections import defaultdict
from pathlib import Path

def get_files_by_size(target_object) -> list[list[Path]]:
    """
    Check file size and groups their by their size
    :param target_object: Instance cotaining the path
    :return: List of file paths
    """
    size_map = defaultdict(list)
    path_string = target_object.get_target_folder

    for item in Path(path_string).rglob('*'):
        if item.is_file():
            try:
                size = item.stat().st_size
                size_map[size].append(item)
            except OSError:
                continue

    return [group for group in size_map.values() if len(group) > 1]