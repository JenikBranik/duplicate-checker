import unittest
import tempfile
import os
import shutil
from pathlib import Path
from src.utils.targetfolder import TargetFolder
from src.lib.filesbysize import get_files_by_size

class TestFilesBySize(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Clean up test fixtures"""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_empty_folder_returns_empty_list(self):
        """
        Test that empty folder returns empty list
        """
        target = TargetFolder(self.temp_dir)
        result = get_files_by_size(target)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_two_files_same_size(self):
        """
        Test that two files with same size are grouped together
        """
        file1 = os.path.join(self.temp_dir, "file1.txt")
        file2 = os.path.join(self.temp_dir, "file2.txt")

        Path(file1).write_text("same size")
        Path(file2).write_text("same size")

        target = TargetFolder(self.temp_dir)
        result = get_files_by_size(target)

        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 2)
        self.assertIn(Path(file1), result[0])
        self.assertIn(Path(file2), result[0])

    def test_multiple_files_different_sizes(self):
        """
        Test that files with different sizes are not grouped
        """
        file1 = os.path.join(self.temp_dir, "file1.txt")
        file2 = os.path.join(self.temp_dir, "file2.txt")
        file3 = os.path.join(self.temp_dir, "file3.txt")

        Path(file1).write_text("small")
        Path(file2).write_text("medium content")
        Path(file3).write_text("very large content here")

        target = TargetFolder(self.temp_dir)
        result = get_files_by_size(target)

        self.assertEqual(len(result), 0)