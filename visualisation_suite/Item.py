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
        return f"[V:{self.value}|S:{int(self.selected)}|C:{int(self.compared)}]"
    
    def __lt__(self, other) -> bool:
        ''' Overload < operator to compare item values'''
        return self.value < other.value
    
    def __gt__(self, other) -> bool:
        ''' Overload > operator to compare item values'''
        return self.value > other.value
    
    def __le__(self, other) -> bool:
        ''' Overload <= operator to compare item values'''
        return self.value <= other.value

    def __ge__(self, other) -> bool:
        ''' Overload >= operator to compare item values'''
        return self.value >= other.value

    def draw(self,window) -> None:
        ''' Draw sorting item to pygame window'''
        pygame.draw.rect(window, self.colour, [self.x, self.y, self.width, self.height])
    
    def update(self) -> None:
        ''' Update X coordinate of the sorting item'''
        self.x = self.index*self.width

    def set_selected(self, is_selected) -> None:
        ''' self.selected setter'''
        self.selected = is_selected

    def set_compared(self, is_compared) -> None:
        ''' self.compared setter'''
        self.compared = is_compared

    def set_index(self, index) -> None:
        ''' self.index setter'''
        self.index = index


if __name__ == "__main__":
    # create 2 items with different values
    i1 = Item(height=0, width=0, value=1, index=0, x=0, y=0, colour=(0,0,0), selected=False, compared=False)
    i2 = Item(height=0, width=0, value=2, index=0, x=0, y=0, colour=(0,0,0), selected=False, compared=False)
    # test operator overload
    print(i1 > i2) # expect False
    print(i1 < i2) # expect True

