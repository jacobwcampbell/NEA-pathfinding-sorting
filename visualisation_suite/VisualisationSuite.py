from PathfindingSuite import PathfindingSuite
from SortingSuite import SortingSuite

class VisualisationSuite():
    
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        self.choose_application()

    def choose_application(self) -> None:
        choice = input("1. Sorting 2. Pathfinding \n: ") # Take user input
        isvalid, program = self.validate_choice(choice)
        if not isvalid:
            print("Invalid Choice. Choices must be either the program number or name. \n")
            self.choose_application()
        self.program() # Call corresponding load function

    def validate_choice(self,choice) -> tuple(bool, function):
        if choice.isdigit():
            if choice == "1":
                return True, self.load_sorting
            elif choice == "2":
                return True, self.load_pathfinding
            return False, None
        if choice.upper() == "SORTING":
            return True, self.load_sorting
        elif choice.upper() == "PATHFINDING":
            return True, self.load_pathfinding
        return False, None
    
    def load_pathfinding(self) -> None:
        print("Pathfinding Suite has been successfully loaded!")    
    
    def load_sorting(self) -> None:
        print("Sorting Suite has been successfully loaded!")
