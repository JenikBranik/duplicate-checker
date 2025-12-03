import unittest
import tempfile
import shutil

from src.utils.targetfolder import TargetFolder

class TestTargetFolder(unittest.TestCase):

    def test_valid_folder_initialization(self):
        """
        Valid input test
        """
        temp_dir = tempfile.mkdtemp()

        try:
            target = TargetFolder(temp_dir)
            self.assertEqual(target.get_target_folder, temp_dir)
        finally:
            shutil.rmtree(temp_dir)

    def test_non_existent_folder_raises_error(self):
        """
        Test for non-existent folder
        """
        path = "Nahodna/slozka/exe"

        with self.assertRaises(FileNotFoundError):
            TargetFolder(path)


if __name__ == '__main__':
    unittest.main()