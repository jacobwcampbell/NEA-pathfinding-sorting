import pygame
import json
import sys

from Collection import Collection

class SortingSuite():
    
    def __init__(self) -> None:
        self.window = None
        self.items = None
        self.array_size = None
        self.config_colours = None
        self.dimensions = None

    def run(self) -> None:
        '''Set up the application and then run it.'''
        self.setup()
        self.main_loop()

    def setup(self) -> None:
        '''Call the functions associated with loading configuration
        values and creating the basic pygame structure'''
        # load config values from external file
        config = self.load_config() 
        # assign config values to class attributes
        self.array_size = config["array_size"] 
        self.config_colours = config["config_colours"]
        self.dimensions = config["dimensions"]
        # initialize pygame
        self.init_pygame()
        # create pygame window
        self.window = pygame.display.set_mode(config["dimensions"])
        # create collection object
        self.items = Collection(
        array_size=self.array_size,
        config_colours=self.config_colours,
        dimensions=self.dimensions)
        # generate bars to sort
        self.items.generate_items()
        # randomly shuffle bars to sort
        self.items.shuffle_items()


    def main_loop(self) -> None:
        '''Main Loop of the Program'''
        while True:
            # handle user input
            self.handle_input()
            # update the sorting items according to the sorting algorithm
            self.items.update()
            # draw the new frame
            self.draw()

    def draw(self) -> None:
        '''Draw a Frame'''
        # fill the screen with the background colour
        self.window.fill(self.config_colours["col_background"])
        # pass a reference of the screen to the sorting items
        self.items.draw(self.window)

    def handle_input(self) -> None:
        '''Handle user Input'''
        for event in pygame.event.get():
            # check whether a sorting algorithm isn't taking place 
            # and there if is a key being pressed
            if event.type == pygame.KEYDOWN:
                if not self.items.get_sorting():
                # user selection of sorting algorithm
                    if event.key == pygame.K_b:
                        self.items.select_sorting("B")
                    elif event.key == pygame.K_m:
                        self.items.select_sorting("M")
                    elif event.key == pygame.K_q:
                        self.items.select_sorting("Q")
                    elif event.key == pygame.K_i:
                        self.items.select_sorting("I")
                # check whether user is selecting a reset
                if event.key == pygame.K_r:
                    # call reset method of items
                    self.items.reset()

    def load_config(self) -> dict:
        '''Load the configuration file for the sorting suite. '''
        # open the file using a context manager
        with open("sortingconfig") as file:
            config = json.load(file)
        if not self.validate_config(config):
            print("Please Correct Config File")
            sys.exit()
        return config

    def validate_config(self, config) -> bool:
        '''Validate the configuration file for the sorting suite. '''
        # check that the number of items is greater than or equal 2 and report invalid if not
        if config["array_size"] < 2:
            print("Invalid Array Size")
            return False
        # check that the number of config colours is exactly 5 and report invalid if not
        if len(config["config_colours"]) != 5:
            print("5 Config Colours Must Be Specified")
            return False
        # check that every config colour has 3 values in its array and report invalid if not
        for key in config["config_colours"].keys():
            if len(config["config_colours"][key]) != 3:
                print("Config Colour Must Contain 3 0-255 RGB Values")
                return False
        # check that the dimensions array is exactly 2 elements and report invalid if not
        if len(config["dimensions"])!= 2:
            print("Invalid Windows Dimensions")
            return False
        return True
    
    def init_pygame(self) -> None:
        pygame.init()


if __name__ == "__main__":
    sorting = SortingSuite()
    pygame.init()
    sorting.items=Collection()
    window = pygame.display.set_mode((100,100))
    # sorting.setup() 
    while True:
        sorting.handle_input()

