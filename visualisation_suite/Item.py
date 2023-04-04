import pygame

class Item():
    ''' Sorting Item Class'''

    def __init__(self, height, width, value, index, x, y,colour, selected, compared) -> None:
        ''' Construct a new sorting item.'''
        self.height = height
        self.width = width
        self.value = value
        self.index = index
        self.x = x
        self.y = y
        self.colour = colour
        self.selected = selected
        self.compared = compared
        # create pygame rectangle surface object
        self.surface = pygame.Surface((self.width,self.height))

    def __str__(self) -> str:
        ''' Return a user friendly string abstraction of the sorting item, used for development of sorting algorithms.'''
        return f"[Val: {self.value} Index: {self.index} Selected: {self.selected} Compared: {self.compared}]"
    
    def __lt__(self, other):
        ''' Overload < operator to compare item values'''
        return self.value < other.value
    
    def __gt__(self, other):
        ''' Overload > operator to compare item values'''
        return self.value > other.value

    def draw(self,window) -> None:
        ''' Draw sorting item to pygame window'''
        print("Item Successfully Drawn")

    def set_selected(self, is_selected) -> None:
        ''' self.selected setter'''
        self.selected = is_selected

    def set_compared(self, is_compared) -> None:
        ''' self.compared setter'''
        self.compared = is_compared

    def set_index(self, index) -> None:
        ''' self.index setter'''
        self.index = index


