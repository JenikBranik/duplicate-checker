from pathlib import Path
from src.lib.calculatehash import calculate_hash

class FileHasher:
    @staticmethod
    def process_group(file_paths: list[Path]):
        """
        A function that goes through a list of files and groups them by hash
        :return: list of duplicates
        """
        groups = {}
        final_duplicates = []

        for path in file_paths:
            file_hash = calculate_hash(path)

            if file_hash not in groups:
                groups[file_hash] = []

            groups[file_hash].append(str(path))

        for group in groups.values():
            if len(group) > 1:
                final_duplicates.append(group)

        return final_duplicates