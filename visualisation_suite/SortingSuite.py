class SortingSuite():
    
    def __init__(self) -> None:
        self.window = None
        self.items = None
        self.array_size = None
        self.config_colours = None
        self.dimensions = None

    def run(self) -> None:
        '''Sets up the application and then runs it.'''
        self.setup()
        self.main_loop()

    def setup(self) -> None:
        '''Calls the functions associated with loading configuration
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
        self.items = Collection(array_size=self.array_size,
         config_colours=self.config_colours, dimensions=self.dimensions)
        # generate bars to sort
        self.items.generate_items()
        # randomly shuffle bars to sort
        self.items.shuffle_items()


    def main_loop(self) -> None:
        pass

    def draw(self) -> None:
        pass

    def handle_input(self) -> None:
        pass

    def load_config(self) -> dict:
        pass

    def validate_config(self, config) -> bool:
        pass

    def init_pygame(self) -> None:
        pass


