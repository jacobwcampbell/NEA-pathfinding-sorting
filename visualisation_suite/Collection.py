import random

from Item import Item

class Collection():
    '''A Class that represents a container of items to be sorted'''

    def __init__(self, array_size, config_colours, dimensions) -> None:
        '''Initialise Collection Class'''
        # print("Collection Initialised")
        # Array of sorting item objects
        self.items = None
        # Current sorting algorithm
        self.sorting_algorithm = None
        # Current sorting algorithm generator
        self.sorting_algorithm_gen = None
        # Is sorting? boolean
        self.sorting = None
        # Number of sorting items
        self.array_size = array_size
        # Dictionary of user-defined colours
        self.config_colours = config_colours
        # Visual width of bars used to represent sorting items
        self.bar_width = None
        # Size of screen
        self.window_width, self.window_height = dimensions
        # Map of strings to sorting algorithms
        self.sorting_algorithms = {
            "B":self.bubblesort,
            "M":self.mergesort,
            "Q":self.quicksort,
            "I":self.insertionsort
        }
        print("Sucessfully Initialised!")

    @staticmethod
    def calculate_bar_width(window_width, array_size) -> float:
        return window_width/array_size
    
    def generate_items(self) -> None:
        '''Populate the Collection Classes Array with Item Objects'''
        # print("Collection's Generate Items Called")
        # Calculate the visual width of all items
        self.bar_width = Collection.calculate_bar_width(self.array_size, self.window_width)
        # Create the empty array for items
        self.items = []
        for i in range(self.array_size):
            # Height is the visual representation of the items number, 
            # sorting visually from big-small/small-big
            height = i + 1
            # Width is precalculated and the same for all items
            width = self.bar_width
            # Value is the items 'number' it is used for sorting
            value = i + 1
            # Index is the items place in the array
            index = i
            # The items inital x position is calculated by its width multiplied by its index
            x = i * self.bar_width
            # The items initial y position is the height of the window minus the height of 
            # the object. This is because pygame's coordinate system has the top left corner
            # as 0,0 so we need to move the drawing to the bottom then back up by the size
            # of the object
            y = self.window_height - height
            # Initial colour is user defined
            colour = self.config_colours["col_item_default"]
            # Is the item currently selected?
            selected = False
            # Is the item currently being compared to the selected item?
            compared = False
            # Create the item with this iteration's calculated attributes shown above
            item = Item(
                heigh = height,
                width = width,
                value = value,
                index = index,
                x = x,
                y = y,
                colour = colour,
                selected = selected,
                compared = compared
            )
            # Add item to items array
            self.items.append(item)

    def shuffle_items(self) -> None:
       ''' Randomly Shuffle Array of Items'''
       # print("Collection's Shuffle Items Called")
       random.shuffle(self.items)
    
    def draw(self, window) -> None:
        ''' Draw sorting items to window '''
        for item in self.items:
            # call each items draw method
            item.draw(window)

    def update(self) -> None:
        ''' Attempt to access the next frame by accessing the sorting algorithm generator'''
        # Only update when a sorting algorithm is taking place
        if self.sorting:
            try:
                # Access next iteration of the generator
                next(self.sorting_algorithm_gen())
            # If the sorting algorithm has finished, set sorting bool to false
            except StopIteration:
                self.sorting = False

    def select_sorting(self, algorithm) -> None:
        ''' Selects a sorting algorithm from user input and creates its generator.'''
        self.sorting = True
        self.sorting_algorithm = self.sorting_algorithms[algorithm]
        # Calling the sorting algorithm function for the first
        # time gives us the generator
        self.sorting_algorithm_gen = self.sorting_algorithm()
    
    def get_sorting(self) -> bool:
        ''' Returns whether a sorting algorithm is currently taking place.'''
        return self.sorting
    
    def bubblesort(self) -> bool:
        print("Bubblesort Selected")

    def mergesort(self) -> bool:
        print("Mergesort Selected")

    def insertionsort(self) -> bool:
        print("Insertionsort Selected")

    def quicksort(self) -> None:
        print("Quicksort Selected")

    def partition(self, items, low, high) -> bool:
        pass

    def reset(self) -> None:
        ''' Reset the sorting process and generate new items'''
        self.sorting = False
        self.generate_items()
        self.shuffle_items()


if __name__ == "__main__":
    c = Collection(
        array_size = 5,
        config_colours = {
        "col_background":[255,255,255],
        "col_item_default":[255, 0, 0],
        "col_item_selected":[0, 0, 255],
        "col_item_compared":[255, 255, 0],
        "col_item_sorted":[0, 255, 0]
        },
        dimensions=(100,100),
    )
    c.generate_items()
    c.shuffle_items()
    c.select_sorting("B")   # Expect "Bubblesort selected"
    c.select_sorting("M")   # Expect "Mergesort selected"
    c.select_sorting("Q")   # Expect "Quicksort selected"
    c.select_sorting("I")   # Expect "Insertionsort selected"


