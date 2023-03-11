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
            print("Invalid Choice. Choices must be either the program number or name. \n") # Invalid choice handling
            self.choose_application()                                                      
        program() # Call corresponding load function                                  

    def validate_choice(self,choice) :
        if not isinstance(choice, str): # Rejects Non-String datatypes
            return False, None
        if choice.isdigit(): # Validate numerical choices
            if choice == "1":
                return True, self.load_sorting
            elif choice == "2":
                return True, self.load_pathfinding
            return False, None
        if choice.upper() == "SORTING": # Validate alphabetical choices
            return True, self.load_sorting
        elif choice.upper() == "PATHFINDING":
            return True, self.load_pathfinding
        return False, None
    
    def load_pathfinding(self) -> None:
        print("Pathfinding Suite has been successfully loaded!")    
    
    def load_sorting(self) -> None:
        '''Loads the sorting suite.'''
        app = SortingSuite()
        app.run()


if __name__ == '__main__':
    v = VisualisationSuite()
    print(v.validate_choice("1")) # Valid/Boundary
    print(v.validate_choice("2")) # Valid/Boundary
    print(v.validate_choice("0")) # Invalid
    print(v.validate_choice(25)) # Erroneous
    print(v.validate_choice("Pathfinding")) # Valid
    print(v.validate_choice("PaTHfinDInG")) # Valid - Mixed Case
    print(v.validate_choice("Hacking")) # Invalid

