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
     Notes: 
       -(0,0) is the TL piece, indices increase down and to the right.
       -All square tuples are [row_num, col_num].
            
     Data Members:
       size: an int >= 4 to represent the NxN size of the board
       matrix: an NxN numpy array, representing the 2d game board.  Values 
               are ints and can be <EMPTY> for empty, <RED> for red, 
               and <BLUE> for blue."""

  def __init__(self, size):
    """Constructor: initializes an instance of class Board.  Size
         is used to set the game board to be an NxN matrix.
       Precondition: size is an int >= 4."""
    assert(isinstance(size, int) and size >= 4), "size is not an int > 4"
    self.size= size
    self.matrix= np.zeros((size, size), dtype=np.int)

  def validSquare(self, square):
    """Raises AssertionError if square is not a valid tuple of ints of 
         value 0 <= i < self.size."""
    assert(isinstance(square[0], int) and isinstance(square[1], int))
    assert(square[0] >= 0 and square[1] >= 0)
    assert(square[1] < self.size and square[1] < self.size)

  def getRow(self, row_num):
    """Returns: the specified row of the board as a list of ints.
       Precondition: row_num is an int between 0 <= row_num < size."""
    assert(isinstance(row_num,int) and row_num >= 0 and row_num < self.size)
    return self.matrix[row_num]

  def getCol(self, col_num):
    """Returns: the specified column of the board as a list of ints.
       Precondition: col_num is an int between 0 <= col_num < size."""
    assert(isinstance(col_num,int) and col_num >= 0 and col_num < self.size)
    col= []
    for row in self.matrix:
      col.append(row[col_num])
    return col
  
  def fillSquare(self, square, color):
    """Sets the specified square to have <color>'s color.
       Precondition: <square> is a tuple of ints of 0 <= i < size,
         color is EMPTY, RED, or BLUE."""
    self.validSquare(square)
    self.matrix[square]= color
 
  ##############Functions to determine validity of square placement 

  #Rule 1: equal # of color pieces in each row/col
  def equalColorLine(self, lst):
    """Returns: True if there are an equal number of red and blue pieces in
         the list; False otherwise.
       Precondtion: lst is a 1d list of ints representing a row or col."""
    colors= {RED: 0, BLUE: 0, EMPTY: 0}
    for i in lst:
      colors[i]+= 1
    return colors[RED] == colors[BLUE]
  
  def equalColorBoard(self):
    """Returns: True if there are an equal number of red and blue pieces in
         each row and column in the board; False otherwise."""
    equal= True
    for i in range(self.size):
      l= [self.equalColorLine(self.getRow(i)), self.equalColorLine(self.getCol(i))]
      if False in l:
        equal= False
        break
    return equal

  #Rule 2: no three colors in a row in each row/col
  def noThreesLine(self, lst):
    """Returns: True if the current row/col contains no 3 adjacent squares
         of the same color; False otherwise.
       Precondition: lst is a 1d list of ints representing a row or col."""
    valid= True
    for i in range(len(lst) - 2):
      if lst[i] == lst[i+1] and lst[i] == lst[i+2]:
        valid= False
        break
    return valid

  def noThreesBoard(self):
    """Returns: True if there are no adjacent three color squares in the
         entire board; False otherwise."""
    valid= True
    for i in range(self.size):
      l= [self.noThreesLine(self.getRow(i)), self.noThreesLine(self.getCol(i))]
      if False in l:
        valid= False
        break
    return valid

  #Rule 3: no two rows/cols are the same
  
  #DO UNIQUE COL AND UNIQ ROW SEPARATE, COMBINE IN BOARD FUNC


  def uniqueBoard(self):
    """Returns: True if no two rows or cols are equal in the whole board;
         False otherwise."""
    return 
 





############################  Script Code  ################################

if __name__ == "__main__":
  b= Board(4)
  b.matrix[0]= [1,1,2,2]
  b.matrix[1]= [1,1,2,2]
  b.matrix[2]= [2,2,1,1]
  b.matrix[3]= [2,2,1,1]

  print b.matrix
  print b.equalColorBoard()
  print b.noThreesBoard()
