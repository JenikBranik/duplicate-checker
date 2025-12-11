from finder.scanner import ParallelScanner
from views.chosefolder import chose_folders


class DuplicateController:
    """
    Main logic of program
    """
    def start_program(self):
        print("Chose file: (To end the selection, click close.)")
        try:
            target_folder = chose_folders()
            app = ParallelScanner(target_folder)
            app.scan()
            print(app)

        except (FileNotFoundError, NotADirectoryError, ValueError) as e:
            print(f"\nError: {e}")