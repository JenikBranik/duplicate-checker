from multiprocessing import freeze_support
from manager import DuplicateController

if __name__ == "__main__":
    freeze_support()
    program = DuplicateController()
    program.start_program()