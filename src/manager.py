from utils.targetfolder import TargetFolder
from finder.scanner import ParallelScanner
from views.chosefile import chose_file


class DuplicateController:
    """
    Main logic of program
    """
    def start_program(self):
        print("Chose file: ")
        try:
            target_folder = chose_file()
            app = ParallelScanner(target_folder)
            app.scan()
            print(app)

        except (FileNotFoundError, NotADirectoryError, ValueError) as e:
            print(f"\nError: {e}")
