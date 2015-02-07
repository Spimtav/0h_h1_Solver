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
       matrix: an NxN 2d numpy array, representing the 2d game board. Values 
               are ints and can be <EMPTY> for empty, <RED> for red, 
               and <BLUE> for blue.
       mutable: an NxN 2d numpy array, representing the mutability of each
               square on the board.  Values are bools, and can be True for
               mutability and False for immutability."""

  def __init__(self, size):
    """Constructor: initializes an instance of class Board.  Size
         is used to set the game board to be an NxN matrix.
       NOTE: asks user for input to set the initial, immutable square colors.
       Precondition: size is an int >= 4."""
    assert(isinstance(size, int) and size >= 4), "size is not an int > 4"
    self.size= size
    self.matrix= np.zeros((size, size), dtype=np.int)
    mutable= []
    for i in range(self.size):
      row= []
      for j in range(self.size):
        row.append(True)
      mutable.append(row)
    self.mutable= mutable
    self.initialSquares()
    
  def parseInput(self, s):
    """Returns: all individual pieces of s that are separated by /, in
         correct types, as a list if input is formatted correctly.
         Otherwise, will recurse on self.initialSquares.
       Precondition: s is a string.
       Ex: parseInput("4/2/red") -> [4, 2, RED]."""
    if s == "q":
      return s
    l= []
    #Extract first datum, the x-coord, and add to list.
    if "/" not in s:
      print "Invalid format."
      self.initialSquares()
    x_coord= s[:s.index("/")]
    if not x_coord.isdigit():
      print "Invalid X-coordinate."
      self.initialSquares()
    x_coord= int(x_coord)
    if x_coord < 0 or x_coord >= self.size:
      print "X-coordinate out of board size range."
      self.initialSquares()
    l.append(x_coord)
    s= s[s.index("/") + 1:]
    #Extract second datum, the y-coord, and add to list.
    if "/" not in s:
      print "Invalid format."
      self.initialSquares()
    y_coord= s[:s.index("/")]
    if not y_coord.isdigit():
      print "Invalid Y-coordinate."
      self.initialSquares()
    y_coord= int(y_coord)
    if y_coord < 0 or y_coord >= self.size:
      print "Y-coordinate out of board size range."
      self.initialSquares()
    l.append(y_coord)
    s= s[s.index("/") + 1:]
    #Extract third datum, the color, and add to list.
    if s == "red":
      l.append(RED)
    elif s == "blue":
      l.append(BLUE)
    else:
      print "Invalid color. Please choose 'red' or 'blue'"
      self.initialSquares()
    #Everything worked, so return l.
    return l

  def initialSquares(self):
    """Asks user for the starting square locations and colors, and then
         makes those changes to <self.matrix> and <self.mutable>."""
    print ""
    print "Pick your board's initial square locations and colors."
    print "Please enter the x-coord, y-coord, and color, separating each with a single '/'."
    print "Note: (0, 0) is top-left corner."
    x= ""
    while x != "q":
      x= raw_input("X-coord/Y-coord/Color (either 'red' or 'blue'), or 'q' to quit: ").lower().strip()
      if x != "q":
        data= self.parseInput(x) #If passed, data is all correct and in list form
        self.matrix[data[0]][data[1]]= data[2]
        self.mutable[data[0]][data[1]]= False

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

  def getColMatrix(self):
    """Returns: 2d int list corresponding to the column matrix of
         <self.matrix> (rows and cols switched)."""
    col_mat= []
    for i in range(self.size):
      col_mat.append(self.getCol(i))
    return col_mat

  def getAllLines(self):
    """Returns: 2d int list corresponding to all rows and columns
         of the matrix represented by <self.matrix>, mostly to
         make iteration easy."""
    lines= []
    for row in self.matrix:
      lines.append(row)
    for col in self.getColMatrix():
      lines.append(col)
    return lines
  
  def fillSquare(self, square, color):
    """Sets the specified square to have <color>'s color.
       Precondition: <square> is a tuple of ints of 0 <= i < size,
         color is EMPTY, RED, or BLUE."""
    self.validSquare(square)
    self.matrix[square]= color

  def switchColor(self, square):
    """Sets the specified square to have the opposite color.
       Precondition: <square> is a tuple of ints of 0 <= i < size."""
    if self.matrix[square] == RED:
      self.matrix[square]= BLUE
    elif self.matrix[square] == BLUE:
      self.matrix[square]= RED
 
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

  def uniqueRows(self):
    """Returns: True if all rows in the board are unique; False otherwise."""
    matrix= self.matrix.tolist()  #Need to do in order to check membership
    unique= True
    for i in range(self.size):
      if matrix[i] in matrix[i+1:]:
        unique= False
        break
    return unique

  def uniqueCols(self):
    """Returns: True if all cols in the board are unique; False otherwise."""
    #Flip matrix for easy comparison
    col_mat= []
    for i in range(self.size):
      col_mat.append(self.getCol(i))
    #Do the uniq comparison
    unique= True
    for i in range(self.size):
      if col_mat[i] in col_mat[i+1:]:
        unique= False
        break
    return unique

  def uniqueBoard(self):
    """Returns: True if no two rows or cols are equal in the whole board;
         False otherwise."""
    return self.uniqueRows() and self.uniqueCols()

  def isSolved(self):
    """Returns: True if this board is solved; False otherwise."""
    return self.equalColorBoard() and self.noThreesBoard() and self.uniqueBoard()
 
  ################### Useful functions for local search scoring
  
  #three main funcs, one per rule - totalnum threes, totalnum unequal, totalnum identicals
  #then unite into main scoring func. then the rest should be easy!

  def numUnequal(self):
    """Returns: the total number of rows and columns that have an unequal
         number of red and blue pieces, as an int."""
    unequal= 0
    lines= self.getAllLines()    
    #Row and col color equality counts
    for line in lines:
      d= {RED: 0, BLUE: 0}
      for square_color in line:
        d[square_color]+= 1
      if d[RED] != d[BLUE]:
        unequal+= 1
    return unequal

  def numThrees(self):
    """Returns: the total number of three-in-a-row pieces on the entire
         board, as an int."""
    threes= 0
    lines= self.getAllLines()
    #Row and col threes counts
    for line in lines:
      for i in range(self.size - 2):
        if line[i] == line[i+1] and line[i] == line[i+2]:
          threes+= 1
    return threes 

  def numDups(self):
    """Returns: the total number of duplicate columns and rows in
         <self.matrix>, as an int. For any multiset of duplicates, this 
         method treats one as being normal and the other len(multiset)-1
         as duplicates.  Ex: numDuplicate([1,1,2]) = 1 if this method
         worked on single lists."""
    dups= 0
    #Num unique rows
    matrix= self.matrix.tolist()
    colmat= self.getColMatrix()
    for i in range(self.size):
      if matrix[i] in matrix[i+1:]:
        dups+= 1
        matrix
      if colmat[i] in colmat[i+1:]:
        dups+= 1
    return dups

  def score(self):
    """Returns: int representing the sum of the three individual score
         values: <numUnequal> + <numThrees> + <numDups>. Boards closer
         to the solution have lower values, so score is essentially
         a measure of the number of mistakes in the matrix."""
    return self.numUnequal() + self.numThrees() + self.numDups()

  def printScore(self):
    """Prints the individual score values and total score in an 
         easy-to-read format."""
    print "Number unequal color lines: " + str(self.numUnequal())
    print "Number threes: " + str(self.numThrees())
    print "Number duplicate lines: " + str(self.numDups())
    print "Total score: " + str(self.score())
    

############################  Script Code  ################################

if __name__ == "__main__":
  b= Board(4)
  b.matrix[0]= [2,2,1,2]
  b.matrix[1]= [1,2,1,2]
  b.matrix[2]= [1,1,2,2]
  b.matrix[3]= [2,1,2,1]

  print b.matrix
  #print b.equalColorBoard()
  #print b.noThreesBoard()
  #print b.uniqueBoard()
  b.printScore()
