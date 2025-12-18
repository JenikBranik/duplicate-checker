import unittest
import tempfile
import shutil
import os
from src.utils.targetfolder import TargetFolder

class TestTargetFolder(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures"""
        self.temp_dir = tempfile.mkdtemp()

    def test_valid_folder_initialization(self):
        """
        Valid input test
        """
        target = TargetFolder(self.temp_dir)
        self.assertEqual(target.get_target_folder, self.temp_dir)

    def test_valid_folder_with_subdirectories(self):
        """
        Test initialization with folder containing subdirectories
        """
        subdir = os.path.join(self.temp_dir, "subdir")
        os.makedirs(subdir)
        target = TargetFolder(self.temp_dir)
        self.assertEqual(target.get_target_folder, self.temp_dir)

    def test_non_existent_folder_raises_error(self):
        """
        Test for non-existent folder
        """
        path = "Nahodna/slozka/exe"

        with self.assertRaises(FileNotFoundError):
            TargetFolder(path)

    def test_invalid_input_type_none(self):
        """
        Test if input is None
        """
        with self.assertRaises(TypeError):
            TargetFolder(None)

    def test_invalid_input_type_dict(self):
        """
        Test if input is dictionary
        """
        with self.assertRaises(TypeError):
            TargetFolder({"path": self.temp_dir})

    def test_empty_string_raises_error(self):
        """
        Test empty string input
        """
        with self.assertRaises(FileNotFoundError):
            TargetFolder("")

    def test_set_target_folder_validates_path(self):
        """
        Test that set_target_folder validates the path
        """
        target = TargetFolder(self.temp_dir)
        new_valid_dir = tempfile.mkdtemp()
        try:
            target.set_target_folder(new_valid_dir)
            self.assertEqual(target.get_target_folder, new_valid_dir)
        finally:
            shutil.rmtree(new_valid_dir)