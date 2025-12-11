import multiprocessing
import os
import time
from collections import defaultdict

from src.utils.targetfolder import TargetFolder
from src.finder.hasher import FileHasher
from src.lib.filesbysize import get_files_by_size


class ParallelScanner:
    def __init__(self, target: list[TargetFolder]):
        self.target_folder = target
        self.duration = None
        self.duplicates = []

    def scan(self):
        """
        Main method for scanning a file
        """
        start_time = time.time()
        files_grouped_by_size = defaultdict(list)

        for target_folder in self.target_folder:
            groups_in_folder = get_files_by_size(target_folder)

            for group in groups_in_folder:

                try:
                    size = os.path.getsize(group[0])
                    files_grouped_by_size[size].extend(group)
                except OSError:
                    pass

        potential_duplicate_files = [group for group in files_grouped_by_size.values() if len(group) > 1]
        cpu_count = multiprocessing.cpu_count()
        final_results = []

        with multiprocessing.Pool(cpu_count) as pool:
            results = pool.map(FileHasher.process_group, potential_duplicate_files)

            for batch in results:
                final_results.extend(batch)

        self.duration = time.time() - start_time
        self.duplicates = final_results

    def __str__(self):
        """
        Dunder method of class ParallelScanner
        :return: returns string with result
        """
        group_number = 1
        final_text = f"Done in {self.duration} sec\n"
        final_text += f"Found {len(self.duplicates)} duplicate groups.\n"

        if not self.duplicates:
            return final_text + "Nothing found"

        for group in self.duplicates:
            final_text += f"\nGroup {group_number}:\n"

            for path in group:
                final_text += f"  - {path}\n"

            group_number += 1

        return final_text