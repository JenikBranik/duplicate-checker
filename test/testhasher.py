import unittest
import tempfile
import os
import shutil
from pathlib import Path

from src.finder.hasher import FileHasher


class TestFileHasher(unittest.TestCase):


    def setUp(self):
        """
        Set up test fixtures
        """
        self.temp_dir = tempfile.mkdtemp()


    def tearDown(self):
        """
        Clean up test fixtures
        """
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_empty_list_returns_empty_list(self):
        """
        Test that empty list returns empty list
        """
        result = FileHasher.process_group([])

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_single_file_returns_empty_list(self):
        """
        Test that single file returns empty list (no duplicates)
        """
        test_file = os.path.join(self.temp_dir, "single.txt")
        Path(test_file).write_text("content")

        result = FileHasher.process_group([Path(test_file)])

        self.assertEqual(len(result), 0)

    def test_two_different_files_returns_empty_list(self):
        """
        Test that two different files return empty list
        """
        file1 = os.path.join(self.temp_dir, "file1.txt")
        file2 = os.path.join(self.temp_dir, "file2.txt")

        Path(file1).write_text("content 1")
        Path(file2).write_text("content 2")

        result = FileHasher.process_group([Path(file1), Path(file2)])

        self.assertEqual(len(result), 0)

    def test_empty_files_grouped(self):
        """
        Test that empty files are detected as duplicates
        """
        file1 = os.path.join(self.temp_dir, "empty1.txt")
        file2 = os.path.join(self.temp_dir, "empty2.txt")

        Path(file1).touch()
        Path(file2).touch()

        result = FileHasher.process_group([Path(file1), Path(file2)])

        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 2)

