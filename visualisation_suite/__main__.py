import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
# hide the "hello from the pygame community message"

from VisualisationSuite import VisualisationSuite

if __name__ == '__main__': # Ran Only when code is executed as a script not module
    app = VisualisationSuite() # Creates an instance of the Root Visualisation Suite App Class
    app.run() # Loads the choice functionality for the user






