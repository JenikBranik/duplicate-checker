from pathlib import Path

class TargetFolder:
    def __init__(self, target_folder):
        self.set_target_folder(target_folder)

    @property
    def get_target_folder(self):
        """
        Method returning a value of path
        :return: target folder path
        """
        return self.target_folder

    def set_target_folder(self,target_folder):
        """
        Method setting a value of path and checking
         if the target folder is really existing
        :param target_folder: target folder path
        """
        path_object = Path(target_folder)
        if not isinstance(target_folder, str):
            raise TypeError("Folder has to be chosen")
        if not path_object.is_dir():
            raise FileNotFoundError(f"Chosen folder aint folder")
        self.target_folder = target_folder
