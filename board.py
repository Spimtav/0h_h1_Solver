#board.py
#Maximillian Tinati
#January 31, 2015
"""Class to contain the game state data of an 0h_h1 game."""

import numpy as np

############################  Constants  ###################################

#Colors for output
cRED= "\033[41m"   #ANSI red color background
cBLUE= "\033[46m"  #ANSI cyan color background, easier contrast w/the red
cRESET= "\033[0m"  #ANSI reset background to white

#Game piece values
EMPTY= 0
RED= 1
BLUE= 2

############################  Board Class  #################################

class Board(object):
  """Class board represents an instance of an 0h_h1 game.  Contains rules
       for proper piece placement and maintains matrix of all filled/empty
       squares.
     Data Members:
       matrix: an NxN numpy array, representing the 2d game board.  Values 
               are ints and can be <EMPTY> for empty, <RED> for red, 
               and <BLUE> for blue."""

  def __init__(self, size):
    """Constructor: initializes an instance of class Board.  Size
         is used to set the game board to be an NxN matrix.
       Precondition: size is an int >= 0."""
    assert(isinstance(size), int and size >= 0), "size is not an int > 0"
    self.matrix= np.zeros((size, size), dtype=np.int)
    print self.matrix












############################  Script Code  ################################

if __name__ == "__main__":
  Board()
