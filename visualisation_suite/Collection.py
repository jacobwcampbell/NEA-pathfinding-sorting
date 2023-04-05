import random
import time

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
        self.bar_width = Collection.calculate_bar_width(self.window_width, self.array_size)
        # Create the empty array for items
        self.items = []
        for i in range(self.array_size):
            # Height is the visual representation of the items number, 
            # sorting visually from big-small/small-big
            # this multiplier stops 0 height items scales them relative to the screen
            # the biggest item here will be the height of the window
            height = (i + 1)*(self.window_height/self.array_size)
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
                height = height,
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
       self.update_indicies()
    
    def update_indicies(self) -> None:
        ''' Update indices of sorting items'''
        for item in self.items:
            item.set_index(self.items.index(item))

    
    def draw(self, window) -> None:
        ''' Draw sorting items to window '''
        for item in self.items:
            # call each items draw method
            item.draw(window)

    def update(self) -> None:
        '''Attempt to access the next frame by accessing the sorting algorithm generator'''
        # Only update when a sorting algorithm is taking place
        for item in self.items:
                self.update_indicies()
                item.update()
        if self.sorting:
 
            try:
                # Access next iteration of the generator
                next(self.sorting_algorithm_gen)
                time.sleep(0.5)
            # If the sorting algorithm has finished, set sorting bool to false
            except StopIteration:
                self.sorting = False
                #print("FINISHED")
        else:
            #print("NO SORTING")
            pass

    def select_sorting(self, algorithm) -> None:
        '''Selects a sorting algorithm from user input and creates its generator.'''
        self.sorting = True
        self.sorting_algorithm = self.sorting_algorithms[algorithm]
        # Calling the sorting algorithm function for the first
        # time gives us the generator
        self.sorting_algorithm_gen = self.sorting_algorithm()
    
    def get_sorting(self) -> bool:
        '''Returns whether a sorting algorithm is currently taking place.'''
        return self.sorting
    
    def bubblesort(self) -> bool:
        ''' Bubblesort the sorting items in ascending order'''
        n = len(self.items)
        swapped = False
        # Each i loop is per pass
        for i in range(n-1):
            # Each j loop is per element per pass
            swapped = False
            for j in range(n-i-1):
                # Select the current and next item as the selected item and compared item
                # This is used for drawing purposes
                self.items[j].set_selected(True)
                self.items[j+1].set_compared(True)
                yield True
                if self.items[j] > self.items[j+1]:
                    swapped = True
                    print(f"Items {j} and {j+1} Swapped")
                    self.items[j], self.items[j+1] = self.items[j+1], self.items[j]

                # Get a new frame after each item is selected
                
                # Deselect both items after the new frame
                self.items[j].set_selected(False)
                self.items[j].set_compared(False)
                self.items[j+1].set_selected(False)
                self.items[j+1].set_compared(False)
                
            #print(f"Pass {i} Completed")
            if not swapped:
                #print("Algorithm Completed")
                break
            

    def mergesort(self) -> bool:
        width = 1
        n = len(self.items)
        while width < n:
            l=0
            while n > 1:
                r = min(l+(width*2-1), n-1)
                m = min(l+width-1,n-1)
                self.merge(l,m,r)
                yield True
                l += width*2
            width *=2
            
    
    def merge(self, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2
        for i in range(n1):
            L[i] = self.items[l + i]
        for i in range(n2):
            R[i] = self.items[m + i + 1]
        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                self.items[k] = L[i]
                i += 1
            else:
                self.items[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            self.items[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            self.items[k] = R[j]
            j += 1
            k += 1

    def insertionsort(self) -> bool:
        ''' Insertionsort the sorting items in ascending order'''
        n = len(self.items)
        for i in range(1,n):
            key = self.items[i]
            self.items[i].set_selected(True)
            j = i-1
            while (j >= 0) and key < self.items[j]:
                self.items[j+1] = self.items[j]
                j -= 1
            self.items[j+1] = key
            yield True
            self.items[i].set_selected(False)
            
            


    def quicksort(self) -> None:
        print("Quicksort Selected")

    def partition(self, items, low, high) -> bool:
        pass

    def reset(self) -> None:
        '''Reset the sorting process and generate new items'''
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
    for item in c.items: print(item, end=" ")
    print("\n\n")
    c.select_sorting("M")
    for _ in range(100):
        c.update()
        for item in c.items: print(item,end=", ")
        print("\n")

