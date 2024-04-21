import stddraw # the stddraw module is used as a basic graphics library
from color import Color # used for coloring the tile and the number on it
from point import Point # used for representing the position of the tile
import copy as cp # the copy module is used for copying tile positions
import math # math module that provides mathematical functions
import random
import numpy as np

# Class used for representing numbered tiles as in 2048
class Tile:
   # Class attributes shared among all Tile objects
   # ---------------------------------------------------------------------------
   # value used for the thickness of the boxes (boundaries) around the tiles
   boundary_thickness = 0.004
   # font family and size used for displaying the tile number
   font_family, font_size = "Arial", 14

   # Constructor that creates a tile at a given position with 2 as its number
   def __init__(self, position = Point(0, 0)): # (0, 0) is the default position
      # Assigns the random number of the tile 2 or 4 for initial
      numbers = [2, 4]
      # Sets a background color for each possible number
      self.colors = [Color(233, 245, 228), Color(210, 235, 213), Color(185, 224, 198), Color(160, 210, 180), Color(135, 195, 165),
                Color(110, 180, 150), Color(85, 165, 135), Color(60, 150, 120), Color(35, 135, 105), Color(25, 120, 90), Color(15, 105, 75), Color(5, 90, 60)]
      self.num = int(np.random.choice(numbers, 1))
      self.number = self.num
      # set the colors of the tile
      # for background numbers on tile and tile boundaires
      self.background_color = self.colors[int(math.log2(self.num))-1]
      self.foreground_color = Color(59, 41, 28) 
      self.boundary_color = Color(59, 41, 28)
      # set the position of the tile as the given position
      self.position = Point(position.x, position.y)

   # Setter method for the position of the tile
   def set_position(self, position):
      # set the position of the tile as the given position
      self.position = cp.copy(position)

   # Getter method for the position of the tile
   def get_position(self):
      # return the position of the tile
      return cp.copy(self.position)

   # Method for moving the tile by dx along the x axis and by dy along the y axis
   def move(self, dx, dy):
      self.position.translate(dx, dy)

   # Method for drawing the tile
   def draw(self, position = None):
      if position is None:
          position = self.position
      # draw the tile as a filled square
      stddraw.setPenColor(self.background_color)
      stddraw.filledSquare(self.position.x, self.position.y, 0.5)
      # draw the bounding box of the tile as a square
      stddraw.setPenColor(self.boundary_color)
      stddraw.setPenRadius(Tile.boundary_thickness)
      stddraw.square(self.position.x, self.position.y, 0.5)
      stddraw.setPenRadius()  # reset the pen radius to its default value
      # draw the number on the tile
      stddraw.setPenColor(self.foreground_color)
      stddraw.setFontFamily(Tile.font_family)
      stddraw.setFontSize(Tile.font_size)
      stddraw.boldText(self.position.x, self.position.y, str(self.number))

   # As the number on the tile increases the color on tile gets darker
   #to convert the number on the tile to the index of the color --> math.log2(num)-1 used
   def updateColor(self, num):
      self.background_color = self.colors[int(math.log2(num)) - 1]